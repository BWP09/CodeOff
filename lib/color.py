import colorama as col

class Color:
    class Codes:
        RED  = col.Fore.RED
        LRED = col.Fore.LIGHTRED_EX
        YLW  = col.Fore.YELLOW
        LYLW = col.Fore.LIGHTYELLOW_EX
        GRN  = col.Fore.GREEN
        LGRN = col.Fore.LIGHTGREEN_EX
        CYN  = col.Fore.CYAN
        LCYN = col.Fore.LIGHTCYAN_EX
        BLU  = col.Fore.BLUE
        LBLU = col.Fore.LIGHTBLUE_EX
        MGT  = col.Fore.MAGENTA
        LMGT = col.Fore.LIGHTMAGENTA_EX
        BLK  = col.Fore.BLACK
        GRY  = col.Fore.LIGHTBLACK_EX

        RST  = col.Fore.WHITE

    def __init__(self) -> None:
        self.prefix = "<"
        self.suffix = ">"

        self.replace = {
            f"{self.prefix}RED{self.suffix}": col.Fore.RED,
            f"{self.prefix}LRED{self.suffix}": col.Fore.LIGHTRED_EX,
            
            f"{self.prefix}YLW{self.suffix}": col.Fore.YELLOW,
            f"{self.prefix}LYLW{self.suffix}": col.Fore.LIGHTYELLOW_EX,
            
            f"{self.prefix}GRN{self.suffix}": col.Fore.GREEN,
            f"{self.prefix}LGRN{self.suffix}": col.Fore.LIGHTGREEN_EX,

            f"{self.prefix}CYN{self.suffix}": col.Fore.CYAN,
            f"{self.prefix}LCYN{self.suffix}": col.Fore.LIGHTCYAN_EX,
            
            f"{self.prefix}BLU{self.suffix}": col.Fore.BLUE,
            f"{self.prefix}LBLU{self.suffix}": col.Fore.LIGHTBLUE_EX,
            
            f"{self.prefix}MGT{self.suffix}": col.Fore.MAGENTA,
            f"{self.prefix}LMGT{self.suffix}": col.Fore.LIGHTMAGENTA_EX,
            
            f"{self.prefix}BLK{self.suffix}": col.Fore.BLACK,
            f"{self.prefix}GRY{self.suffix}": col.Fore.LIGHTBLACK_EX,

            f"{self.prefix}RST{self.suffix}": col.Fore.WHITE,


            f"{self.prefix}F_BLD{self.suffix}": "\033[1m",
            f"{self.prefix}F_UND{self.suffix}": "\033[4m",

            f"{self.prefix}F_CLR{self.suffix}": "\033[2J",
            f"{self.prefix}F_RST{self.suffix}": "\033[0m",
        }

    def parse(self, text: str):
        text += f"{self.prefix}RST{self.suffix}{self.prefix}F_RST{self.suffix}"
        
        for k, v in self.replace.items():
            text = text.replace(k, v)

        return text
    
    def strip_color(self, text: str):
        for k in self.replace.keys():
            text = text.replace(k, "")

        return text