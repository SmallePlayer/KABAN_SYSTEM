import requests


url = "http://192.168.1.3:80"

def resp_get(url, endpoint):
    response = requests.get(f"{url}{endpoint}")
    response.raise_for_status()
    data = response.json()
    return data

def resp_params_get(url, endpoint, params):
    response = requests.get(f"{url}{endpoint}", params=params)
    response.raise_for_status()
    data = response.json()
    return data 

def resp_post(url, endpoint):
    response = requests.post(f"{url}{endpoint}")
    response.raise_for_status()
    data = response.json()
    return data

def get_info(url):
    endpoint = "/printer/info"
    return resp_get(url, endpoint)

def pause_print(url):
    endpoint = "/printer/print/pause"
    return resp_post(url, endpoint)

def resume_print(url):
    endpoint = "/printer/print/resume"
    return resp_post(url, endpoint)

def cancle_print(url):
    endpoint = "/printer/print/cancle"
    return resp_post(url, endpoint)

def extruder_info(url):
    endpoint = "/printer/objects/query"
    params = {
        "objects": {
        "extruder": None,
        "toolhead": ["temperature", "target"]
        }
    }
    return resp_params_get(url, endpoint, params)