"""
Test library functions to plot data
"""
import pytest
import numpy as np

from data_plotting import (
    perform_linear_regression,
    get_correlation_coefficients,
)


# Define sets of test cases.
perform_linear_regression_cases = [
    # test simple linear relationship
    ([np.array([1, 2, 3]), np.array([2, 4, 6])], (2, 0, 1)),

    # test tick and humidity relationship
    ([np.array([66.18246313, 71.42232345, 68.20874646, 73.4316989,  71.90363023]),
     np.array([3, 45, 38, 53, 99])], (8.5897, -555.6533, .736)),
]

get_correlation_coefficients_cases = [
    # test simple case
    ([["x_1", "x_2"], [np.array([1, 2, 3]), np.array([-1, -2, -3])],
     np.array([2, 4, 6])], {"x_1": 1, "x_2": -1}),

    # test correlations for all datasets
    ([['Humidity', 'Precipitation'],
      [np.array([66.18246313, 71.42232345, 68.20874646, 73.4316989,  71.90363023]),
     np.array([1.45133333, 4.53193548, 3.569, 1.76935484, 2.14483871])],
        np.array([3, 45, 38, 53, 99])], {"Humidity": .736, "Precipitation": 0.05}),
]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("data,values", perform_linear_regression_cases)
def test_perform_linear_regression(data, values):
    """
    Test that perform_linear_regression returns expected values.
    Args:
        data: A list with the values being a list of the numpy arrays
            of the independent data and a numpy array of the dependent data.
        coefficients: A dictionary with the keys as the strings of the
            names of the independent datasets, and the values as the
            Pearson correlaction coefficients (r_value).
    """
    assert perform_linear_regression(data[0], data[1]) == values


@pytest.mark.parametrize("data,coefficients", get_correlation_coefficients_cases)
def test_get_correlation_coefficients(data, coefficients):
    """
    Test that get_correlation_coefficients returns correct coefficients.
    Args:
        data: A list with the values being a list of the string names
            of the independent data, a list of the numpy arrays of the
            independent data, and a numpy array of the dependent data.
        coefficients: A dictionary with the keys as the strings of the
            names of the independent datasets, and the values as the
            Pearson correlaction coefficients (r_value).

    """
    assert get_correlation_coefficients(
        data[0], data[1], data[2]) == coefficients
