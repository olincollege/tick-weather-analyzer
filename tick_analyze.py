def tick_process(data):
    """
    Isolate and process only necessary tick data
    
    Args:
        data: data frame ##edit later##
    Returns:
        - necessary_data: a 2D array with the second column as the total amount of tick
        for a month and the first column as the month and year the data is collected
    """
    dates = data[0].loc[:,"collectDate"].values.tolist()
    amounts = data[0].loc[:,"individualCount"].values.tolist()
    # for row in data.columns:
    #     dates = row[4]
    #     amounts = row[14]
    
    necessary_data = [[],[]]
    for i in range(len(dates)):
        if dates[i][:7] == dates[i-1][:7]:
            total_amount += amounts[i]
        elif dates[i][:7] != dates[i-1][:7]:
            if i != 0:
                necessary_data[0].append(dates[i-1][:7])
                necessary_data[1].append(total_amount)
            total_amount = 0
    return necessary_data