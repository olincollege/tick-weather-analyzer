"""
Test library functions to combine data for each dataset.
"""
import pytest

from data_analyzer import (
    humidity_analyze,
    precipitation_analyze,
    tick_analyze
)


# Define sets of test cases.
humidity_analyze_cases = [
    
]

precipitation_analyze_cases = [
    
]

tick_analyze_cases = [

]



# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("data,average_humidity", humidity_analyze)
def test_humidity_analyze(data, average_humidity):
    """
    Test that humidity_analyze averages correctly over a month.
    Args:
        data: A dataframe with all of the relative humidity data
            and the date at which it was taken.
        average_humidity: A dataframe with a column for the month and
            a column for the respective average relative humidity.
    """
    assert humidity_analyze(data) == average_humidity


@pytest.mark.parametrize("data,average_precipitation", precipitation_analyze)
def test_precipitation_analyze(data, average_precipitation):
    """
    Test that precipitation_analyze averages correctly over a month.
    Args:
        data: A dataframe with all of the precipitation data
            and the date at which it was taken.
        average_precipitation: A dataframe with a column for the month and
            a column for the respective average precipitation.
    """
    assert precipitation_analyze(data) == average_precipitation

@pytest.mark.parametrize("data,sum_ticks", tick_analyze)
def test_tick_analyze(data, sum_ticks):
    """
    Test that tick_analyze sums correctly over a month.
    Args:
        data: A dataframe with all of the tick data
            and the date at which it was taken.
        average_humidity: A dataframe with a column for the month and
            a column for the sum of ticks.
    """
    assert tick_analyze(data) == sum_ticks
