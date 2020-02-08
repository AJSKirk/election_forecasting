import sklearn.metrics


def average_brier_score(outcome, forecast_probs, weights=None):
    y_true = [outcome] * len(forecast_probs)
    return sklearn.metrics.brier_score_loss(y_true, forecast_probs, weights)
