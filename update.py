import requests
import json
from time import sleep
import os

update_url = ""

update_modules = []

def check_updates():
    # Git update file
    git_update = requests.get(update_url).json()

    # Local update file
    with open('src/json/updates.json', 'r') as json_local_file:
        json_local_data = json.load(json_local_file)

    for i
    json_local_data["src"][file_name]["id"] = git_json[setup_update_type][file_name]["id"]

    with open('src/json/local_update.json', 'w') as json_id_file:
        json.dump(json_local_data, json_id_file)

