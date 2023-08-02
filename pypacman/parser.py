from ast import literal_eval
from typing import Dict, List, Tuple
import re

class Parser:
    def __init__(self) -> None:
        self.packages: Dict[str, Tuple[str, bool, List[str]]] = {}
    
    def _parse_line(self, line: str):
        split_line = line.split(";")
        
        if len(split_line) != 4:
            raise ValueError("Length of line is incorrect")
        
        name, version, strict, overrides = split_line
        strict = literal_eval(strict)
        overrides = overrides.replace("None", "").split(",")
        while "" in overrides:
            overrides.remove("")
        
        self.packages[name] = (version, strict, overrides)
        
    def parse_file(self, filename: str) -> None:
        with open(filename, "r") as pacman_file:
            lines = pacman_file.readlines()
            
        regex = re.compile("\s+") # type: ignore ... VS Code doesn't like \s
        for line in lines:
            whitespace = re.findall(regex, line.strip())
            cleaned_line = line.strip().split("#")[0]
            if len(cleaned_line) == 0:
                continue
            
            for match in sorted(whitespace, key=lambda x:len(x), reverse=True):
                cleaned_line = cleaned_line.replace(match, ";")
                
            self._parse_line(cleaned_line)
        
if __name__ == "__main__":
    parser = Parser()
    parser.parse_file("test.pacman")