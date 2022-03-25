import pandas as pd

def humidity_analyze(data):
    """
    Isolate and process only necessary humidity data by averaging all
    values for each month
    
    Args:
        data: Relative humidity dataframe, downloaded from neon_data_tools

    Returns:
        necessary_data: a dataframe with the second column as the average
        humidity over every day of a month & the first column as the month
        and year the corresponding data on the second column is collected
    
    """
    #Convert contents of "startDateTime" to a datetime object
    data["startDateTime"] = pd.to_datetime(data["startDateTime"])
    data.set_index("startDateTime", inplace = True)

    #Average the humidity for each month
    avg_humidity = data['RHMean'].resample('M').mean()

    #Return array with the month and average relative humidity for each month
    return avg_humidity

def precipitation_analyze(data):
    """
    Isolate and process only necessary precipitation data by adding total
    precipitation for each day and then averaging the totals for each month
    
    Args:
        data: Precipitation dataframe, downloaded from neon_data_tools

    Returns:
        necessary_data: a 2D array with the second column as the average
        precipitation over every day of a month & the first column as the month
        and year the corresponding data on the second column is collected
    
    """
    #Convert contents of "startDateTime" to a datetime object
    data["startDateTime"] = pd.to_datetime(data["startDateTime"])
    data.set_index("startDateTime", inplace = True)
    
    #Add the total precipitation for each day
    precipitation = data["priPrecipBulk"].resample('D').sum()

    #Average the precipitation for the month using the total of each day
    precipitation = precipitation.resample('M').mean()

    #Return array with the month and average precipitation for each month
    return precipitation

def tick_analyze(data):
    """
    Isolate and process only necessary tick data
    
    Args:
        data: a list containing the stacked dataframe of all the information
    Returns:
        necessary_data: a 2D array with the second row as the total amount of tick
        for a month and the first row as the month and year the data is collected
    """
    # Collect dates and tick data from the dataframe containing ticks data (data[0])
    dates = data[0].loc[:,"collectDate"].values.tolist()
    amounts = data[0].loc[:,"individualCount"].values.tolist()
    
    # Initialize return list
    necessary_data = [[],[]]

    # Loop through data
    for i in enumerate(dates):
        # Combine ticks data from the same month
        if dates[i][:7] == dates[i-1][:7]:
            total_amount += amounts[i]
        elif dates[i][:7] != dates[i-1][:7]:
            # Add total amount per month at the end of a month
            if i != 0:
                necessary_data[0].append(dates[i-1][:7])
                necessary_data[1].append(total_amount)
            # Reset counter
            total_amount = 0
    return necessary_data