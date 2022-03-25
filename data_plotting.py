import pandas as pd
from neon_data_tools import download_data
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def perform_linear_regression(independent_data, tick_data):
    slope, intercept, r_value, p_value, standard_error = stats.linregress(independent_data, tick_data)
    return slope, intercept, r_value, p_value, standard_error

def plot_line_of_best_fit(independent_data, tick_data):
    slope, intercept, r_value, p_value, standard_error = perform_linear_regression(independent_data, tick_data)
    plt.scatter(independent_data, tick_data)
    plt.plot(independent_data, slope * independent_data + intercept)
    plt.text(1, max(tick_data) - 1, 'y = ' + '{:.2f}'.format(intercept) + ' + {:.2f}'.format(slope) + 'x', size=12)
    plt.show()

def plot_correlation_coefficients(datasets, independent_datasets, tick_data):
    correlations = {}
    bar_width = 0.35
    for index, data in enumerate(independent_datasets):
        slope, intercept, r_value, p_value, standard_error = perform_linear_regression(data, tick_data)
        correlations[datasets[index]] = r_value
    plt.bar(datasets, list(correlations.values()), bar_width)
    plt.xlabel("Dataset")
    plt.ylabel("Correlation Coefficient")
    plt.title("Correlation Coefficients of Datasets and Tick Population")
    plt.show()

def plot_line_chart(x, y, value):
    plt.plot(x, y)
    plt.title(f'{value} data over time')
    plt.xlabel('Date')
    plt.ylabel(f'{value}')
    plt.show()
