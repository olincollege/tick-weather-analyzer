import requests
import json
import os
import pandas as pd


# store the substrings that appear in the names of the files desired for each dataset
NAME_OF_DESIRED_FILE = {
    "ticks": "taxonomyProcessed",
    "relative humidity": "060.030.RH_30min",
    "precipitation": "900.000.030.PRIPRE_30min"
}


def get_data_urls(dpID, site, date, package="basic"):
    """
    Return the urls and the names of the data for the dataset at the given month.

    Args:
        dpID: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        date: A string that contains the year and month of the data
            requested.
        package: A string that contains the type of data required, with the
            default value being basic as opposed to expanded.

    Returns:
        urls: A list of string containing the urls obtained from requesting the
            data for the given dataset.
        names: A list of strings containing the names of the files found at each
            of the aforementioned urls.
    """
    base_url = "http://data.neonscience.org/api/v0/data/"
    neon_data = requests.get(base_url + dpID + "/" + site + "/" + date + "?package=" + package)
    neon_data_json = neon_data.json()
    urls = [neon_data_json["data"]["files"][i]["url"] for i in range(len(neon_data_json["data"]["files"]))]
    names = [neon_data_json["data"]["files"][i]["name"][28:] for i in range(len(neon_data_json["data"]["files"]))]
    # print(names)
    return urls, names


def download_data(dataset, dpID, site, date, package="basic"): 
    """
    Download the desired data and return the name of the file in which the
    data is stored. 

    Args:
        dataset: A string that says which dataset is being downloaded.
        dpID: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        date: A string that contains the year and month of the data
            requested.
        package: A string that contains the type of data required, with the
            default value being basic as opposed to expanded.

    Returns:
        A string containing the file name where the data is stored.
    """
    # create a folder for the dataset
    new_path = dpID 
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    # get the urls and names of the files pertaining to the dataset  
    urls, names = get_data_urls(dpID, site, date, package)
    # print(names)

    # get the index of the file name that contains the substrng that 
    # identifies it as a desired file
    desired_index = [index for index, name in enumerate(names) if NAME_OF_DESIRED_FILE[dataset] in name][0]
    # print(desired_index)
    requested_file = requests.get(urls[desired_index], allow_redirects=True)

    # save the data into a new file
    file_name = names[desired_index]
    file_path = f"{new_path}/{file_name}"
    open(file_path, 'wb').write(requested_file.content)
    return file_name


def get_file_names(file_names, dataset, dpID, site, date, package="basic"):
    """
    Download the desired data and add the file name to the dictionary of file names.

    Args:
        file_names: A dictionary containing the dataset names as keys and
            list of strings of the saved file names for the datset as the
            values.
        dataset: A string that says which dataset is being downloaded.
        dpID: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        date: A string that contains the year and month of the data
            requested.
        package: A string that contains the type of data required, with the
            default value being basic as opposed to expanded.

    Returns:
        A dictionary containing all of the file names for each dataset.
    """
    name = download_data(dataset, dpID, site, date, package)
    file_names[dataset].append(f"{dpID}/{name}")
    return file_names


def get_data_over_time(file_names, dataset, dpID, site, dates, package="basic"):
    """
    Download the desired data over a range of time.

    Args:
        file_names: A dictionary containing the dataset names as keys and
            list of strings of the saved file names for the datset as the
            values.
        dataset: A string that says which dataset is being downloaded.
        dpID: A string that is the unique dataproduct ID for the dataset.
        site: A string that contains the four letter code of the dataset.
        dates: A list of strings that contains all of the years and months 
            of the data requested.
        package: A string that contains the type of data required, with the
            default value being basic as opposed to expanded.
    """
    for month in dates:
        get_file_names(file_names, dataset, dpID, site, month, package="basic")


def create_stacked_dataframe(file_paths):
    """
    Combine the data for each dataset into one dataframe.

    Args:
        file_paths: A list of the file paths of the stored data for
            the given dataset.
    
    Returns:
        A dataframe of the combines data for the dataset.
    """
    return pd.concat(map(pd.read_csv, [file_path for file_path in file_paths]), ignore_index = True)


def download_all_datasets(file_names, datasets, dpIDs, site, dates, package="basic"):
    """
    Download the desired data and return all of the stacked dataframes

    Args:
        file_names: A dictionary containing the dataset names as keys and
            list of strings of the saved file names for the datset as the
            values.
        datasets: A list of string that contains all of the datasets to
            be downloaded.
        dpIDs: A dictionary with the keys as the strings of the names of the
            datasets and the keys as the strings of the unique data product ID.
        site: A string that contains the four letter code of the dataset.
        dates: A list of strings that contains all of the years and months of
            the data requested.
        package: A string that contains the type of data required, with the
            default value being basic as opposed to expanded.

    Returns:
        A list of dataframes that represent all of the stacked data for each
        dataset.
    """
    stacked_dataframes = []
    for dataset in datasets:
        get_data_over_time(file_names, dataset, dpIDs[dataset], site, dates, package)
        file_paths = file_names[dataset]
        stacked_dataframes.append(create_stacked_dataframe(file_paths))
    return stacked_dataframes