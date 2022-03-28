"""
Data visulization tools
"""
import pandas as pd
from neon_data_tools import download_data
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def perform_linear_regression(independent_data, tick_data):
    """
    Perform linear regression on data.

    Args:
        independent_data: A numpy array of the independent data.
        tick_data: A numpy array of the total number of ticks per month.
    
    Returns:
        Floats representing the slope, intercept, Pearson correlation coefficient,
        p-value, and standard error of the slope of the linear relationship between
        the data.
    """
    slope, intercept, r_value, p_value, standard_error = stats.linregress(independent_data, tick_data)
    return slope, intercept, r_value, p_value, standard_error

def plot_line_of_best_fit(independent_data, tick_data):
    """
    Plot the line of best fit for the data.

    Plots a scatter plot of the tick_data versus the independent data.
    Adds the line of best fit determined from preform_linear_regression.
    Adds the equation of this line to the plot.

    Args:
        independent_data: A numpy array of the independent data.
        tick_data: A numpy array of the total number of ticks per month.
    
    """
    slope, intercept, r_value, p_value, standard_error = perform_linear_regression(independent_data, tick_data)
    plt.scatter(independent_data, tick_data)
    plt.plot(independent_data, slope * independent_data + intercept)
    plt.text(min(independent_data) + 1, max(tick_data) - 0.3, 'y = ' + '{:.2f}'.format(intercept) + ' + {:.2f}'.format(slope) + 'x', size=12)
    plt.show()

def plot_correlation_coefficients(datasets, independent_datasets, tick_data):
    """
    Plot the correlation coefficients for the data.

    Plots a bar graph with each bar representing the correlation
    coefficient of the given dataset and the tick_data. Uses
    get_correlation_coefficents to determine the correlation coefficients.
    
    Args:
        datasets: A list of strings that represent the names of the
            independent data in their respective order.
        independent_datasets: A list of numpy arrays of the independent data.
        tick_data: A numpy array of the total number of ticks per month.
    """
    bar_width = 0.35
    correlations = get_correlation_coefficients(datasets, independent_datasets, tick_data)
    plt.bar(datasets, list(correlations.values()), bar_width)
    plt.xlabel("Dataset")
    plt.ylabel("Correlation Coefficient")
    plt.title("Correlation Coefficients of Datasets and Tick Population")
    plt.show()

def get_correlation_coefficients(datasets, independent_datasets, dependendent_dataset):
    """
    Gets the correlation coefficients for each dataset.

    Adds the correlation of the given dataset to the dictionary
    representing all of the datasets and their given correlation
    coefficient. Uses perform_linear_regression to get the
    r_value, which is the Pearson correlation coefficent.
    
    Args:
        datasets: A list of strings that represent the names of the
            independent data in their respective order.
        independent_datasets: A list of numpy arrays of the independent data.
        tick_data: A numpy array of the total number of ticks per month.
    
    Returns:
        correlations: A dictionary with each key being the string representing
        the name of the dataset, and the key being the respective correlation
        coefficient.
    """
    correlations = {}
    for index, data in enumerate(independent_datasets):
        slope, intercept, r_value, p_value, standard_error = perform_linear_regression(data, dependendent_dataset)
        correlations[datasets[index]] = r_value
    return correlations

def plot_line_chart(time, dependent_data, value):
    """
    Plot the data over time.

    Plots a line graph of the dependent_data over time.
    
    Args:
        time: A numpy array of datatime objects.
        dependent_data: A numpy array of the values at
            each time step.
    """
    plt.plot(time, dependent_data)
    plt.title(f'{value} data over time')
    plt.xlabel('Date')
    plt.ylabel(f'{value}')
    plt.show()

def data_to_array(data_series):
    """
    Convert the series into a numpy array.
    
    Args:
        data_series: A pandas series with the desired data.
    
    Returns:
        A numpy array of the given data.
    """
    return np.array(data_series)