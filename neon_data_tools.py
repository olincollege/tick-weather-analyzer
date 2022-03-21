import requests
import json
import os
import pandas as pd

INDEX_OF_DESIRED_FILE = {
    "ticks": 5,
    "relative humidity": 6
}

def get_data_urls(dpID, site, dates, package="basic"):
    base_url = "http://data.neonscience.org/api/v0/data/"
    # print(requests.get("http://data.neonscience.org/api/v0/products/"+dpID).json())
    full_url = f""
    neon_data = requests.get("http://data.neonscience.org/api/v0/data/" + dpID + "/" + site + "/" + dates + "?package=" + package)
    #data_parameters = {"dpID": dpID, "site": site, "dates": dates, "package": package}
    #neon_data = requests.get(base_url, params = data_parameters)
    neon_data_json = neon_data.json()
    #print(json.dumps(neon_data_json, indent=4))
    #print(neon_data_json["data"]["files"][0])
    urls = [neon_data_json["data"]["files"][i]["url"] for i in range(len(neon_data_json["data"]["files"]))]
    names = [neon_data_json["data"]["files"][i]["name"][28:] for i in range(len(neon_data_json["data"]["files"]))]
    #print(names)
    #print(requests.get(urls[0]))
    return urls, names

def download_data(dataset, dpID, site, dates, package="basic"): 
    new_path = dpID 
    if not os.path.exists(new_path):
        os.makedirs(new_path)     
    urls, names = get_data_urls(dpID, site, dates, package)
    desired_url_index = INDEX_OF_DESIRED_FILE[dataset]
    requested_file = requests.get(urls[desired_url_index], allow_redirects=True)
    file_name = names[desired_url_index]
    file_path = f"{new_path}/{file_name}"
    open(file_path, 'wb').write(requested_file.content)
    # for i in range(len(urls)):
    #     r = requests.get(urls[i], allow_redirects=True)
    #     file_path = f"{new_path}/{names[i]}"
    #     open(file_path, 'wb').write(r.content)
    return file_name

def get_file_names(file_names, dataset, dpID, site, dates, package="basic"):
    name = download_data(dataset, dpID, site, dates, package)
    file_names[dataset].append(f"{dpID}/{name}")
    return file_names


def create_stacked_csv(file_paths):
    return pd.concat(map(pd.read_csv, [file_path for file_path in file_paths]), ignore_index = True)