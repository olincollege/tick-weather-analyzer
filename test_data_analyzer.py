"""
Test library functions to combine data for each dataset.
"""
import pytest
import neon_data_tools
import pandas as pd
import numpy as np

from data_analyzer import (
    humidity_analyze,
    precipitation_analyze,
    tick_analyze
)

# Define sets of test cases.
humidity_analyze_cases = [
    # test simple case of one month
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40]], columns = ["startDateTime", 'RHMean']),[50]),

    # test that data is averaged at the month level, not the day level
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-01", 20], ["2017-04-02", 40]], columns = ["startDateTime", 'RHMean']),[40]),

]

precipitation_analyze_cases = [
    # test simple case of one month
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40]], columns = ["startDateTime", 'priPrecipBulk']),[50]),

    # test that data is added for each day before being averaged on the month level
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-01", 10], ["2017-04-02", 40]], columns = ["startDateTime", 'priPrecipBulk']),[55]),
]

tick_analyze_cases = [
    # test simple case of one month
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40]], columns = ["collectDate", 'individualCount']),[100]),

    # test that data is added for each day and each month
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-01", 10], ["2017-04-02", 40]], columns = ["collectDate", 'individualCount']),[110]),

]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("data,average_humidity", humidity_analyze_cases)
def test_humidity_analyze(data, average_humidity):
    """
    Test that precipitation_analyze averages correctly over a month.
    Args:
        data: A dataframe with all of the relative humidity data
            and the date at which it was taken.
        average_humidity: A numpy array with the respective average relative humidity.
    """
    assert humidity_analyze(data) == average_humidity

@pytest.mark.parametrize("data,average_precipitation", precipitation_analyze_cases)
def test_precipitation_analyze(data, average_precipitation):
    """
    Test that precipitation_analyze averages correctly over a month.
    Args:
        data: A dataframe with all of the precipitation data
            and the date at which it was taken.
        average_precipitation: A numpy array with the respective average precipitation.
    """
    assert precipitation_analyze(data) == average_precipitation

@pytest.mark.parametrize("data,sum_ticks", tick_analyze_cases)
def test_tick_analyze(data, sum_ticks):
    """
    Test that tick_analyze sums correctly over a month.
    Args:
        data: A dataframe with all of the tick data
            and the date at which it was taken.
        average_humidity: A numpy array with the sum of ticks.
    """
    assert tick_analyze(data) == sum_ticks


# tests for data with multiple months
def test_humidity_analyze_multiple_months():
    """
    Test that humidity_analyze averages correctly over a month.
    """
    data = pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40], ["2017-05-01", 30]], columns = ["startDateTime", 'RHMean'])
    average_humdidity = [50, 30]

    assert humidity_analyze(data).all() == np.array(average_humdidity).all()

def test_precipitation_analyze_multiple_months():
    """
    Test that precipitation_analyze averages correctly over a month.
    """
    data = pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40], ["2017-05-01", 30]], columns = ["startDateTime", 'priPrecipBulk'])
    average_precipitation = [50, 30]

    assert precipitation_analyze(data).all() == np.array(average_precipitation).all()

def test_tick_analyze_multiple_months():
    """
    Test that tick_analyze averages correctly over a month.
    """
    data = pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40], ["2017-05-01", 30]], columns = ["collectDate", 'individualCount'])
    sum_ticks = [100, 30]

    assert tick_analyze(data).all() == np.array(sum_ticks).all()
