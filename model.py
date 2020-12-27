"""Black-Scholes Binary Option Pricing For Non-Dividend Paying Options."""

import numpy as np
import pandas as pd
import scipy.stats as si
import sympy as sy
from sympy.core.evalf import PrecisionExhausted
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()

# S: stock price
# K: strike price
# T: time to maturity
# r: interest rate
# sigma: volatility of underlying asset

def call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)
    
    return call


def put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))

    return put


def options(S, K, T, r, sigma, option):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    result: str = ""

    if option == 'call':
        result = S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)
    elif option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    return result

df = pd.read_excel("TSLA_data.xlsx", engine='xlrd')

print(df.head())

S = df["Last Price"][0]
K = df["Strike"][0]
T = 20/365
r = df["Open Interest"][0] / 100
sigma = df["Implied Volatility"][0]

call_price = call(S, K, T, r, sigma)
print(call_price)