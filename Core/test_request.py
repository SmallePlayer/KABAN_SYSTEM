import requests


url = "http://192.168.1.3:80"

def resp(url, endpoint):
    response = requests.get(f"{url}{endpoint}")
    response.raise_for_status()
    data = response.json()
    return data

def resp_params(url, endpoint, params):
    response = requests.get(f"{url}{endpoint}", params=params)
    response.raise_for_status()
    data = response.json()
    return data 


def get_info(url):
    endpoint = "/printer/info"
    return resp(url, endpoint)

def pause_print(url):
    endpoint = "/printer/print/pause"
    return resp(url, endpoint)

def resume_print(url):
    endpoint = "/printer/print/resume"
    return resp(url, endpoint)

def cancle_print(url):
    endpoint = "/printer/print/cancle"
    return resp(url, endpoint)

def extruder_info(url):
    endpoint = "/printer/objects/query"
    params = {
        "objects": {
        "extruder": None,
        "toolhead": ["temperature", "target"]
        }
    }
    return resp_params(url, endpoint, params)