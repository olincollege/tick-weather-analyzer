"""
Process necessary data from dataframes pulled from the National Ecological Observatory Network
"""
import pandas as pd


def humidity_analyze(data):
    """
    Isolate and process only necessary humidity data by averaging all
    values for each month

    Args:
        data: Relative humidity dataframe, downloaded from neon_data_tools

    Returns:
        necessary_data: a pandas series of the average
        humidity over every day of a month with the month as the
        row labels.

    """
    # Convert contents of "startDateTime" to a datetime object
    data["startDateTime"] = pd.to_datetime(data["startDateTime"])
    data.set_index("startDateTime", inplace=True)

    # Average the humidity for each month
    avg_humidity = data['RHMean'].resample('M').mean()

    return avg_humidity


def precipitation_analyze(data):
    """
    Isolate and process only necessary precipitation data by adding total
    precipitation for each day and then averaging the totals for each month

    Args:
        data: Precipitation dataframe, downloaded from neon_data_tools

    Returns:
        necessary_data: a pandas series of the average
        precipitation over every day of a month with the month as the
        row labels.

    """
    # Convert contents of "startDateTime" to a datetime object
    data["startDateTime"] = pd.to_datetime(data["startDateTime"])
    data.set_index("startDateTime", inplace=True)

    # Add the total precipitation for each day
    precipitation = data["priPrecipBulk"].resample('D').sum()

    # Average the precipitation for the month using the total of each day
    precipitation = precipitation.resample('M').mean()

    # Return array with the month and average precipitation for each month
    return precipitation


def tick_analyze(data):
    """
    Isolate and process only necessary tick data

    Args:
        data: Ticks dataframe, downloaded from neon_data_tools
    Returns:
        necessary_data: a pandas series with the total amount of tick
        for a month and the month as the row labels.
    """
    # Convert contents of "collectDate" to a datetime object
    data["collectDate"] = pd.to_datetime(data["collectDate"])
    data.set_index("collectDate", inplace=True)

    # Sum the ticks for the month
    sum_ticks = data['individualCount'].resample('M').sum()

    return sum_ticks
