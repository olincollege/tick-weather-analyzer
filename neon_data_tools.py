import requests
import json
import os


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
    #print(urls)
    #print(requests.get(urls[0]))
    return urls, names

def download_data(dpID, site, dates, package="basic"): 
    new_path = dpID 
    if not os.path.exists(new_path):
        os.makedirs(new_path)     
    urls, names = get_data_urls(dpID, site, dates, package)
    for i in range(len(urls)):
        r = requests.get(urls[i], allow_redirects=True)
        file_path = f"{new_path}/{names[i]}"
        open(file_path, 'wb').write(r.content)