"""
Test neon_data_tools functions.
"""
import pytest
import numpy as np

from neon_data_tools import (
    create_stacked_dataframe,
    get_dates,
)

# # Define sets of test cases.
# create_stacked_dataframe_cases = [
#     # test tick data
#     ("D")
# ]

get_dates_cases = [
    # Same start/end month and start/end year
    ([1, 1, 2000, 2000], [['2000-01']]),
    # Range of months in same year
    ([5, 8, 1988, 1988], [['1988-05', '1988-06', '1988-07', '1988-08']]),
    # Same month, different years
    ([2, 2, 2000, 2003], [['2000-02'], ['2001-02'], ['2002-02'], ['2003-02']]),
    # Same range of months, different years
    ([4, 8, 2017, 2019], [['2017-04', '2017-05', '2017-06', '2017-07', '2017-08'],
        ['2018-04', '2018-05', '2018-06', '2018-07', '2018-08'],
        ['2019-04', '2019-05', '2019-06', '2019-07', '2019-08']]),
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
# @pytest.mark.parametrize("data,values", create_stacked_dataframe_cases)
# def test_create_stacked_dataframe(data, values):
#     """
#     Test that perform_linear_regression returns expected values.
#     Args:
#         data: A list with the values being a list of the numpy arrays
#             of the independent data and a numpy array of the dependent data.
#         coefficients: A dictionary with the keys as the strings of the
#             names of the independent datasets, and the values as the
#             Pearson correlaction coefficients (r_value).
#     """
#     assert create_stacked_dataframe(data[0], data[1]) == values

@pytest.mark.parametrize("data,values", get_dates_cases)
def test_get_dates(data, values):
    """
    """
    assert get_dates(data[0], data[1], data[2], data[3]) == values

