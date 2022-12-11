import json

def is_exit(check):
    with open('title.json', 'r') as f:
        data = json.load(f)
    try:
        if data[f'{check}']:
            return False
    except KeyError:
        return True

def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["emp_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def to_enter(value):
    with open('title.json', 'r') as f:
        data = json.load(f)
    y = {f"{value}":1}
    data.update(y)
    with open("title.json", "w") as outfile:
        json.dump(data, outfile)
