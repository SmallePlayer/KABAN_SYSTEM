import json

def read_data():
    with open('cam.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_len_data():
    data = read_data()
    return len(data)

def get_data(target_id):
    data = read_data()

    for datas in data:
        if datas['id'] == target_id:
            found_data = datas
            break
        
    if found_data:
        id = datas['id']
        name = datas['name']
        printer_ip = datas['ip']
        camera = datas['camera']

        print(f"id {id} | name {name} | ip {printer_ip} | camera index {camera}")
        return id, name, printer_ip, camera