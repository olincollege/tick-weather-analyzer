def humidity_analyze(data):
    """
    Isolate and process only necessary humidity data
    
    Args:
        data: Relative humidity dataframe, downloaded from neon_data_tools
    Returns:
        - necessary_data: a 2D array with the second column as the average humidity over
        every day of a month & the first column as the month and year the corresponding
        data on the second column is collected
    
    """
    month_days = 0
    for row in data:
        dates = row['startDateTime']
        humidity = row['RHMean']
    necessary_data = [['month', 'average_humidity']]
    for i in dates:
        if dates[i][0:6] == dates[i-1][0:6]:
            total_amount += humidity[i]
            month_days += 1
        elif dates[i][0:6] != dates[i-1][0:6]:
            if i != 0:
                average = total_amount / month_days
                necessary_data += [dates[i-1], average]
            total_amount = 0
    return necessary_data