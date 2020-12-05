import json


def read_config(file='config.json'):
    with open(file) as config_file:
        configuration = json.load(config_file)
    return configuration
