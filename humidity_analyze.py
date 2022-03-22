def humidity_analyze(data):
    """
    Isolate and process only necessary humidity data
    
    Args:
        data: ****TBD****
    Returns:
        - necessary_data: a 2D array with the second column as the average humidity over
        every day of a month & the first column as the month and year the corresponding
        data on the second column is collected
    """
    for row in data:
        dates = row['addSomething']
        humidity = row['addSomething']
    necessary_data = [['month', 'average_humidity']]
    return necessary_data