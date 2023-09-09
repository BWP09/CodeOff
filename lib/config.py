import os.path
import lib.yml as yml

def create_config(config_yml: str, default_values: dict):
    if not os.path.isfile(config_yml):
        yml.create(config_yml, default_values)
    
def reset_config(config_yml: str, default_values: dict):
    yml.write(config_yml, default_values)

def get_config(config_yml: str):
    return yml.read(config_yml)