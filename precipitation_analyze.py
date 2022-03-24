import pandas as pd
def precipitation_analyze(data):
    """
    Isolate and process only necessary precipitation data
    
    Args:
        data: Precipitation dataframe, downloaded from neon_data_tools
    Returns:
        - necessary_data: a 2D array with the second column as the average precipitation over
        every day of a month & the first column as the month and year the corresponding
        data on the second column is collected
    
    """
    month_days = 0
    #dates = pd.DataFrame(data.loc[:,"startDateTime"])
    dates = data.loc[:, 'startDateTime'].values.toList()
    print(dates)
    #precipitation = pd.DataFrame(data.loc[:,['priPrecipBulk']])
    precipitation = data.loc[:, 'priPrecipBulk'].values.toList()
    necessary_data = [['month', 'average_precipitation']]
    for i in dates:
        if dates.iloc[i][1][0:6] == dates.iloc[i-1][1][0:6]:
            total_amount += precipitation[i]
            month_days += 1
        elif dates.iloc[i][1][0:6] != dates.iloc[i-1][1][0:6]:
            if i != 0:
                average = total_amount / month_days
                necessary_data += [dates[i-1], average]
            total_amount = 0
    return necessary_data



    # data["startDateTime"] = pd.to_datetime(data["priPrecipBulk"])
    # data.set_index("startDateTime", inplace = True)
    # precipitation = data.resample('M').sum()
    # return precipitation

