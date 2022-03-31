"""
Import and stylize data pulled from the National Ecological Observatory Network
"""
import os
import requests
import pandas as pd


# store the substrings that appear in the names of the files desired for each dataset
NAME_OF_DESIRED_FILE = {
    "ticks": "taxonomyProcessed",
    "relative humidity": "060.030.RH_30min",
    "precipitation": "900.000.030.PRIPRE_30min"
}


def get_data_urls(dp_id, site, date):
    """
    Return the urls and the names of the data for the dataset at the given month.

    Args:
        dp_id: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        date: A string that contains the year and month of the data
            requested.

    Returns:
        urls: A list of string containing the urls obtained from requesting the
            data for the given dataset.
        names: A list of strings containing the names of the files found at each
            of the aforementioned urls.
    """
    # define the base url for the request
    base_url = "http://data.neonscience.org/api/v0/data/"

    # make a request at the url that follows the NEON data retrieval format
    neon_data = requests.get(base_url + dp_id + "/" +
                             site + "/" + date + "?package=basic")
    # convert the data into JSON
    neon_data_json = neon_data.json()

    # only save the urls and the names of the files
    urls = [neon_data_json["data"]["files"][i]["url"]
            for i in range(len(neon_data_json["data"]["files"]))]
    names = [neon_data_json["data"]["files"][i]["name"][28:]
             for i in range(len(neon_data_json["data"]["files"]))]
    return urls, names


def download_data(dataset, dp_id, site, date):
    """
    Download the desired data and return the name of the file in which the
    data is stored.

    Args:
        dataset: A string that says which dataset is being downloaded.
        dp_id: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        date: A string that contains the year and month of the data
            requested.

    Returns:
        A string containing the file name where the data is stored.
    """
    # create a folder for the dataset
    new_path = dp_id
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    # get the urls and names of the files pertaining to the dataset
    urls, names = get_data_urls(dp_id, site, date)

    # get the index of the file name that contains the substring that
    # identifies it as a desired file
    desired_index = [index for index, name in enumerate(
        names) if NAME_OF_DESIRED_FILE[dataset] in name][0]
    requested_file = requests.get(urls[desired_index], allow_redirects=True)

    # save the data into a new file
    file_name = names[desired_index]
    file_path = f"{new_path}/{file_name}"
    with open(file_path, 'wb') as file:
        file.write(requested_file.content)
    return file_name


def get_file_names(file_names, dataset, dp_id, site, date):
    """
    Download the desired data and add the file name to the dictionary of file names.

    Args:
        file_names: A dictionary containing the dataset names as keys and
            list of strings of the saved file names for the datset as the
            values.
        dataset: A string that says which dataset is being downloaded.
        dp_id: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        date: A string that contains the year and month of the data
            requested.

    Returns:
        A dictionary containing all of the file names for each dataset.
    """
    # get the name of the file containing the data and download the data
    name = download_data(dataset, dp_id, site, date)

    # add the name of the file to the array of file names for the dataset
    file_names[dataset].append(f"{dp_id}/{name}")

    return file_names


def get_data_over_time(file_names, dataset, dp_id, site, dates):
    """
    Download the desired data over a range of time.

    Args:
        file_names: A dictionary containing the dataset names as keys and
            list of strings of the saved file names for the datset as the
            values.
        dataset: A string that says which dataset is being downloaded.
        dp_id: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        dates: A list of strings that contains all of the years and months
            of the data requested.
    """
    # for every month in dates, get the file names and download the data
    # the file names are not needed, so they are not returned
    for month in dates:
        get_file_names(file_names, dataset, dp_id,
                       site, month)


def create_stacked_dataframe(file_paths):
    """
    Combine the data for each dataset into one dataframe.

    Args:
        file_paths: A dictionary of the file paths with the keys as a string of the
            name of the dataset and the values as an array of strings of the file
            paths of the stored data for the given dataset.

    Returns:
        A dataframe of the combines data for the dataset.
    """
    stacked_dataframes = []

    # for every file path for the dataset, combine the data into one dataframe, and append
    # the data to the list of dataframes
    for file_path_names in file_paths.values():
        stacked_dataframes.append(pd.concat(map(
            pd.read_csv, list(file_path_names)), ignore_index=True))
    return stacked_dataframes


def download_all_datasets(file_names, datasets, dp_ids, site, dates):
    """
    Download the desired data and return all of the stacked dataframes

    Args:
        file_names: A dictionary containing the dataset names as keys and
            list of strings of the saved file names for the datset as the
            values.
        datasets: A list of string that contains all of the datasets to
            be downloaded.
        dp_ids: A dictionary with the keys as the strings of the names of the
            datasets and the keys as the strings of the unique data product ID.
        site: A string that contains the four letter code of the dataset.
        dates: A list of strings that contains all of the years and months of
            the data requested.

    Returns:
        A dictionary with the keys as strings of the name of the dataset
        and the values as arrays of strings of the file paths for said dataset.
    """
    # for each dataset, download the data over the the range of time
    for dataset in datasets:
        get_data_over_time(file_names, dataset,
                           dp_ids[dataset], site, dates)

    # return the file names so that they can be used to stack the dataframes later
    return file_names


def get_dates(month_start, month_end, year_start, year_end):
    """
    Generate a list of months over a range of year.

    Args:
        month_start: an integer represents the desired starting month to be included
        month_end: an integer represents the desired last month to be included in one year
        year_start: an integer represents the desired starting year to be included
        year_end: an integer represents the last year to be included in the list

    Returns:
        dates: A list containing smaller lists of a range of desired months in
            a year, the amount of lists corresponds to the desired amount of years
    """
    # Month start: 4
    # Month end: 8
    # Year start: 2017

    dates = []
    year = year_start
    month = month_start
    for i in range(year_end - year_start + 1):
        dates.append([])
        for j in range(month_end - month_start + 1):
            if month < 10:
                dates[i].append(f"{year}-0{month}")
            else:
                dates[i].append(f"{year}-{month}")
            month += 1
            j += 1
        year += 1
        month = month_start
        i += 1
    return dates
