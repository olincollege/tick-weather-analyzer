def tick_process(data):
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