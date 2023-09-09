import lib.color as color, lib.date_time as dt, lib.file as fm, lib.config as conf


cl = color.Color()

log_config = {
    "log_dir": "logs/",
    "print_log_datetime_format": "{month}/{day}/{year2} {hour12}:{minute}:{second} {ampm}",
    "log_file_name_format": "{month}-{day}-{year2}_{hour24}-{minute}-{second}.log",
    "print_format": "[<CYN>#{all_counter} <LMGT>{datetime} {level_color}{level}#{level_counter}<RST>] [{module}<RST>]: {text}",
    "log_format": "[#{all_counter} {datetime} {level}#{level_counter}] [{module}]: {text}",
    "print_to_console": True,
    "log_to_file": True,
    "use_color": True,
}

class Level:
    DBG = 0
    INF = 1
    WRN = 2
    SRS = 3
    ERR = 4
    CRT = 5

    _DBG_CL = "<GRY>"
    _INF_CL = "<GRN>"
    _WRN_CL = "<LYLW>"
    _SRS_CL = "<YLW>"
    _ERR_CL = "<RED>"
    _CRT_CL = "<LRED>"

class Logger:
    def __init__(self, config_yml: str) -> None:   
        self.config_yml = config_yml
        
        conf.create_config(self.config_yml, log_config)
        config = conf.get_config(self.config_yml)

        self.config_log_dir = config["log_dir"]
        self.config_print_log_datetime_format = config["print_log_datetime_format"]
        self.config_log_file_name_format = config["log_file_name_format"]
        self.config_print_format = config["print_format"]
        self.config_log_format = config["log_format"]

        self.config_print_to_console = config["print_to_console"]
        self.config_log_to_file = config["log_to_file"]
        self.config_use_color = config["use_color"]

        self.log_file = self.config_log_dir + dt.parse(self.config_log_file_name_format)

        self._debug_counter = 0
        self._info_counter = 0
        self._warn_counter = 0
        self._serious_counter = 0
        self._error_counter = 0
        self._critical_counter = 0

        self._all_counter = 0
    
    def reload_config(self):
        config = conf.get_config(self.config_yml)

        self.config_print_log_datetime_format = config["print_log_datetime_format"]
        self.config_log_file_name_format = config["log_file_name_format"]
        self.config_print_format = config["print_format"]
        self.config_log_format = config["log_format"]

        self.config_print_to_console = config["print_to_console"]
        self.config_log_to_file = config["log_to_file"]
        self.config_use_color = config["use_color"]
    
    def space_newline(self, base, text):
        return base + text.replace("\n", "\n" + len(cl.strip_color(base)) * " ")
    
    def print_parse(self, level_color: str, level: str, level_counter: int, module: str, text):
        datetime = dt.parse(self.config_print_log_datetime_format)
        print_formatted = self.config_print_format.replace("{all_counter}", str(self._all_counter)).replace("{level_color}", str(level_color)).replace("{level}", str(level)).replace("{level_counter}", str(level_counter)).replace("{datetime}", str(datetime)).replace("{module}", str(module)).replace("{text}", str(text))

        base = print_formatted.removesuffix(text)
        spaced = self.space_newline(base, text)

        return cl.parse(spaced)
    
    def log_parse(self, level: str, level_counter: int, module: str, text):
        datetime = dt.parse(self.config_print_log_datetime_format)
        log_formatted = self.config_log_format.replace("{all_counter}", str(self._all_counter)).replace("{level}", str(level)).replace("{level_counter}", str(level_counter)).replace("{datetime}", str(datetime)).replace("{module}", str(module)).replace("{text}", str(text))

        base = log_formatted.removesuffix(text)
        spaced = self.space_newline(base, text)

        return cl.strip_color(spaced)

    def debug(self, module: str, text):
        self._all_counter += 1
        self._debug_counter += 1

        if self.config_print_to_console:
            if self.config_use_color:
                print(self.print_parse(Level._DBG_CL, "DBG", self._debug_counter, module, text))
            
            else:
                print(self.log_parse("DBG", self._debug_counter, module, text))
        
        if self.config_log_to_file:
            fm.append(self.log_file, self.log_parse("DBG", self._debug_counter, module, text) + "\n")
    
    def info(self, module: str, text):
        self._all_counter += 1
        self._info_counter += 1

        if self.config_print_to_console:
            if self.config_use_color:
                print(self.print_parse(Level._INF_CL, "INF", self._info_counter, module, text))

            else:
                print(self.log_parse("INF", self._info_counter, module, text))
        
        if self.config_log_to_file:
            fm.append(self.log_file, self.log_parse("INF", self._info_counter, module, text) + "\n")
    
    def warn(self, module: str, text):
        self._all_counter += 1
        self._warn_counter += 1

        if self.config_print_to_console:
            if self.config_use_color:
                print(self.print_parse(Level._WRN_CL, "WRN", self._warn_counter, module, text))

            else:
                print(self.log_parse("WRN", self._warn_counter, module, text))

        if self.config_log_to_file:
            fm.append(self.log_file, self.log_parse("WRN", self._warn_counter, module, text) + "\n")
    
    def serious(self, module: str, text):
        self._all_counter += 1
        self._serious_counter += 1

        if self.config_print_to_console:
            if self.config_use_color:
                print(self.print_parse(Level._SRS_CL, "SRS", self._serious_counter, module, text))

            else:
                print(self.log_parse("SRS", self._serious_counter, module, text))

        if self.config_log_to_file:
            fm.append(self.log_file, self.log_parse("SRS", self._serious_counter, module, text) + "\n")
    
    def error(self, module: str, text):
        self._all_counter += 1
        self._error_counter += 1

        if self.config_print_to_console:
            if self.config_use_color:
                print(self.print_parse(Level._ERR_CL, "ERR", self._error_counter, module, text))

            else:
                print(self.log_parse("ERR", self._error_counter, module, text))

        if self.config_log_to_file:
            fm.append(self.log_file, self.log_parse("ERR", self._error_counter, module, text) + "\n")
    
    def critical(self, module: str, text):
        self._all_counter += 1
        self._critical_counter += 1

        if self.config_print_to_console:
            if self.config_use_color:
                print(self.print_parse(Level._CRT_CL, "CRT", self._critical_counter, module, text))
        
            else:
                print(self.log_parse("CRT", self._critical_counter, module, text))

        if self.config_log_to_file:
            fm.append(self.log_file, self.log_parse("CRT", self._critical_counter, module, text) + "\n")

    def log(self, level: int, module: str, text):
        match level:
            case 0: self.debug(module, text)
            case 1: self.info(module, text)
            case 2: self.warn(module, text)
            case 3: self.serious(module, text)
            case 4: self.error(module, text)
            case 5: self.critical(module, text)

class LogParser:
    ...