import yaml, os.path


def create(yml_file: str, content):
    if not os.path.isfile(yml_file):
        open(yml_file, "x").close()

        with open(yml_file, "r+", encoding = "utf-8") as f:
            yaml.dump(content, f, sort_keys = False, width = 1000)

def read(yml_file: str):
    with open(yml_file, "r", encoding = "utf-8") as f:
        return yaml.safe_load(f)

def write(yml_file: str, content: dict):
    with open(yml_file, "w", encoding = "utf-8") as f:
        yaml.dump(content, f, sort_keys = False, width = 1000)

def get_key(yml_file: str, key: str):
    with open(yml_file, "r", encoding = "utf-8") as f:
        try: return yaml.safe_load(f).get(key)
        except: return None

def set_key(yml_file: str, key: str, val):
    with open(yml_file, "r+", encoding = "utf-8") as f:
        yml = yaml.safe_load(f)

        try: yml[key] = val
        except: return

        f.seek(0)
        f.truncate()

        yaml.dump(yml, f, sort_keys = False, width = 1000)

def append(yml_file: str, key: str, val):
    with open(yml_file, "r+", encoding = "utf-8") as f:
        yml = yaml.safe_load(f)

        try: yml[key].append(val)
        except: return

        f.seek(0)
        f.truncate()

        yaml.dump(yml, f, sort_keys = False, width = 1000)