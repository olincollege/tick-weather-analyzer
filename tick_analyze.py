def tick_analyze(data):
    """
    Isolate and process only necessary tick data
    
    Args:

    Returns:

    """
    for row in data:
        dates = row['collectDate']
        amounts = row['individualCount']
    necessary_data = [['month', 'total_ticks']]
    for i in dates:
        if dates[i] == dates[i-1]:
            total_amount += amounts[i]
        elif dates[i] != dates[i-1]:
            if i != 0:
                necessary_data += [dates[i-1], total_amount]
            total_amount = 0