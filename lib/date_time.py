import datetime

date_time_replace = {
    "{day}": "%d",
    "{month}": "%m",
    "{year2}": "%y",
    "{year4}": "%Y",
    "{second}": "%S",
    "{minute}": "%M",
    "{hour12}": "%I",
    "{hour24}": "%H",
    "{ampm}": "%p",
}

def parse(datetime_str: str):
    for k, v in date_time_replace.items():
        datetime_str = datetime_str.replace(k, v)

    return datetime.datetime.today().strftime(datetime_str)