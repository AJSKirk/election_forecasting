import json, click
import pandas as pd


class PointInTime:
    def __init__(self, point_jsons):
        dates = [p['date'] for p in point_jsons]
        assert (len(set(dates))) == 1  # Sanity check to ensure we don't unzip anywhere

        self.date = dates[0]  # Can do WLOG thanks to that assert above
        self.data = {'date': self.date}

        for point in point_jsons:
            party = point['party'].lower()
            for model in point['models']:
                for element in [e for e in point['models'][model].keys() if e != 'distribution']:
                    col_name = '{}_{}_{}'.format(party, model, element)
                    self.data[col_name] = point['models'][model][element]


@click.command()
@click.option('-i', '--input_file', required=True)
@click.option('-o', '--output_file')
@click.option('-p', '--parties', multiple=True)
def main(input_file, output_file, parties):
    """Parses .json object"""

    with open(input_file) as f:
        raw = json.load(f)

    all_points = raw['forecasts']['all']
    target_points = dict()

    for party in parties:
        target_points[party] = [p for p in all_points if p['party'] == party]

    point_in_times = [PointInTime(matched_points) for matched_points in zip(*target_points.values())]
    tabular_data = pd.DataFrame(pit.data for pit in point_in_times)

    tabular_data.to_csv(output_file, header=True, index=False)


if __name__ == "__main__":
    main()
