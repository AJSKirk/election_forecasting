import scipy.stats as stats
import math


def option_price(value_today, payout_threshold, volatility, time_rem):
    """'Naive' pricing from the Clayton paper. For a fixed price today assuming Brownian drift"""
    return 1 - stats.norm.cdf((payout_threshold - value_today) / (volatility * math.sqrt(time_rem)))


def black_scholes_price(value_today, payout_threshold, volatility, time_rem):
    d1 = (math.log(value_today / payout_threshold) + (volatility ** 2 * time_rem / 2)) / (volatility * math.sqrt(time_rem))
    return stats.norm.cdf(d1 - volatility * math.sqrt(time_rem))
