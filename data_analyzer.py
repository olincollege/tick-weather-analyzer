import pandas as pd

def humidity_analyze(data):
    """
    Isolate and process only necessary humidity data
    
    Args:
        data: Relative humidity dataframe, downloaded from neon_data_tools
    Returns:
        - necessary_data: a dataframe with the second column as the average humidity over
        every day of a month & the first column as the month and year the corresponding
        data on the second column is collected
    
    """
    data["startDateTime"] = pd.to_datetime(data["startDateTime"])
    data.set_index("startDateTime", inplace = True)
    precipitation = data['RHMean'].resample('M').mean()
    return precipitation