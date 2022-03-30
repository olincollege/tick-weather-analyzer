"""
Test neon_data_tools functions.
"""
import pytest
import numpy as np

from neon_data_tools import (
    create_stacked_dataframe,
    get_dates,
)

GET_DATES_CASES = [
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

@pytest.mark.parametrize("dates,dates_list", GET_DATES_CASES)
def test_get_dates(dates, dates_list):
    """
    Check that the return value provides the range of desired dates

    Args: 
        dates: A list of desired values, corresponding to: starting month,
            ending month, starting year, ending year for the dates list
        dates_list: A list containing smaller lists of a range of desired months in
            a year, the amount of lists corresponds to the desired amount of years
    """
    assert get_dates(dates[0], dates[1], dates[2], dates[3]) == dates_list
