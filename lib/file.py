def write(file_name: str, content):
    with open(file_name, "w", encoding = "utf-8") as f:
        f.seek(0)
        f.truncate()
        f.write(str(content)) 

def read(file_name: str):
    with open(file_name, "r", encoding = "utf-8") as f:
        return f.read()

def append(file_name: str, content):
    with open(file_name, "a", encoding = "utf-8") as f:
        f.write(str(content))