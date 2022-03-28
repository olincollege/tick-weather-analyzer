"""
Test library functions to plot data
"""
import pytest
import numpy as np

from data_plotting import (
    perform_linear_regression,
    get_correlation_coefficients,
    data_to_array,
)


# Define sets of test cases.
perform_linear_regression_cases = [
    # test simple linear relationship
    ([np.array([1, 2, 3]), np.array([2, 4, 6])], (2, 0, 1)),

    # test tick and humidity relationship
    ([np.array([])])
]

get_correlation_coefficients_cases = [
    
]

data_to_array_cases = [
    
]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("data,values", perform_linear_regression_cases)
def test_perform_linear_regression(data, values):
    """
    Test that perform_linear_regression returns expected values.
    Args:
        
    """
    assert perform_linear_regression(data[0], data[1]) == values


@pytest.mark.parametrize("data,coefficients", get_correlation_coefficients_cases)
def test_get_correlation_coefficients(data, coefficients):
    """
    Test that get_correlation_coefficients returns correct coefficients.
    Args:
        
    """
    assert get_correlation_coefficients(data) == coefficients

@pytest.mark.parametrize("data,array_result", data_to_array_cases)
def test_data_to_array(data, array_result):
    """
    Test that data_to_array correctly converts to numpy array.
    Args:
        
    """
    assert type(data_to_array_cases(data)) == type(array_result)
