"""
Data visulization tools
"""
import matplotlib.pyplot as plt
from scipy import stats


def perform_linear_regression(independent_data, tick_data):
    """
    Perform linear regression on data.

    Args:
        independent_data: A numpy array of the independent data.
        tick_data: A numpy array of the total number of ticks per month.

    Returns:
        Floats representing the slope, intercept, and Pearson correlation
        coefficient of the linear relationship between the data.
    """
    # perform linear regression
    slope, intercept, r_value = stats.linregress(
        independent_data, tick_data)[:3]
    # round the values to four decimal places for readability
    slope = round(slope, 4)
    intercept = round(intercept, 4)
    r_value = round(r_value, 4)

    # return only the needed values
    return slope, intercept, r_value


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
    # perform linear regression
    slope, intercept = perform_linear_regression(
        independent_data, tick_data)[:2]

    # plot the datapoints using a scatter plot
    plt.scatter(independent_data, tick_data)

    # plot the line of best fit using the values from linear regression
    plt.plot(independent_data, slope * independent_data + intercept)

    # add the equation to the plot
    plt.text(min(independent_data) + 1, max(tick_data) - 0.3, 'y = ' +
             '{:.2f}'.format(intercept) + ' + {:.2f}'.format(slope) + 'x', size=12)
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

    # get the correlation coefficents for the datasets
    correlations = get_correlation_coefficients(
        datasets, independent_datasets, tick_data)

    # plot the bar graphs of the correlation coefficients
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
    # get the correlation coefficient for each dataset
    for index, data in enumerate(independent_datasets):
        r_value = perform_linear_regression(
            data, dependendent_dataset)[2]

        # set the value at the key of the dataset to the correlation coefficient
        correlations[datasets[index]] = r_value
    return correlations


def plot_combined_line_graph(time, dependent_datasets, values):
    """
    Plot the data over time.

    Plots a line graph of the data over time.

    Args:
        time: A numpy array of datatime objects.
        dependent_data: A numpy array of the values at
            each time step.
        values: A list of strings containing the names of
            the datasets.
    """
    # set the colors of the lines to be different
    colors = ['r', 'c', 'g']

    # for each dataset, plot the data over time
    for index, value in enumerate(values):
        plt.plot(time, dependent_datasets[index],
                 colors[index], label=value)
    plt.title('Ticks , Relative Humidity, and Precipitation over time')
    plt.xlabel('Date')
    plt.ylabel("Value")
    plt.legend()
    plt.show()
