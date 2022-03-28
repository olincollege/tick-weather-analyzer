"""
Test library functions to combine data for each dataset.
"""
import pytest
import neon_data_tools
import pandas as pd

from data_analyzer import (
    humidity_analyze,
    precipitation_analyze,
    tick_analyze
)
ts = pd.Series([50])
ts.index = ["2017-04-30"]
# TICK_DATAFRAME = neon_data_tools.create_stacked_dataframe(['DP1.10093.001/tck_taxonomyProcessed.2017-04.basic.20211222T024529Z.csv', 'DP1.10093.001/tck_taxonomyProcessed.2017-05.basic.20211221T223943Z.csv', 'DP1.10093.001/tck_taxonomyProcessed.2017-06.basic.20211221T212802Z.csv', 'DP1.10093.001/tck_taxonomyProcessed.2017-07.basic.20211221T222520Z.csv', 'DP1.10093.001/tck_taxonomyProcessed.2017-08.basic.20211222T030656Z.csv'])
# HUMIDITY_DATAFRAME = neon_data_tools.create_stacked_dataframe(['DP1.00098.001/000.060.030.RH_30min.2017-04.basic.20211210T181857Z.csv', 'DP1.00098.001/000.060.030.RH_30min.2017-05.basic.20211210T170044Z.csv', 'DP1.00098.001/000.060.030.RH_30min.2017-06.basic.20211210T174733Z.csv', 'DP1.00098.001/000.060.030.RH_30min.2017-07.basic.20211210T165157Z.csv', 'DP1.00098.001/000.060.030.RH_30min.2017-08.basic.20211210T231107Z.csv'])
# # Define sets of test cases.
humidity_analyze_cases = [
    # test 2017 data
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40]], columns = ["startDateTime", 'RHMean']),[50]),
    # (HUMIDITY_DATAFRAME, pd.Series([66.18246313, 71.42232345, 68.20874646, 73.4316989,  71.90363023]))
]

precipitation_analyze_cases = [
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40]], columns = ["startDateTime", 'priPrecipBulk']),[50]),
]

tick_analyze_cases = [
    (pd.DataFrame([["2017-04-01", 60], ["2017-04-02", 40]], columns = ["collectDate", 'individualCount']),[100])
]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("data,average_humidity", humidity_analyze_cases)
def test_humidity_analyze(data, average_humidity):
    """
    Test that humidity_analyze averages correctly over a month.
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
