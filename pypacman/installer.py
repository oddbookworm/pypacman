from typing import Dict, List, Tuple, Set
from subprocess import Popen
import sys

class Installer:
    def __init__(self, packages: Dict[str, Tuple[str, bool, List[str]]]) -> None:
        self.overridden_packages: Set[str] = set()
        self.overriding_packages: Dict[str, str] = {}
        self.easy_packages: Dict[str, str] = {}
        for data in packages.values():
            for override in data[2]:
                self.overridden_packages.add(override)
                
        for package, data in packages.items():
            if package in self.overridden_packages:
                continue # these packages are getting removed anyway
            
            if data[1]:
                version = data[0]
            else:
                version = "Latest"
    
            if len(data[2]) == 0:
                self.easy_packages.update({package : version})
            else:
                self.overriding_packages.update({package : version})
    
    def _install_packages(self):
        # first install the packages that don't override anything
        installed_modules = list(sys.modules)
        for package, version in self.easy_packages.items():
            if package not in installed_modules:
                install_command = [sys.executable, "-m", "pip", "install", package]
                if version != "Latest":
                    install_command[-1] += f'=={version}'
                    
                p = Popen(install_command)
                p.communicate()
            
            else:
                print(f"Package {package} already installed")
                
        for package in self.overridden_packages:
            p = Popen([sys.executable, "-m", "pip", "uninstall", package, "-y"])
            p.communicate()
            
        for package, version in self.overriding_packages.items():
            install_command = [sys.executable, "-m", "pip", "install", package, "--force"]
            if version != "Latest":
                install_command[-2] += f"=={version}"
            p = Popen(install_command)
            p.communicate()
    
if __name__ == "__main__":
    from parser import Parser # type: ignore
    
    parser = Parser()
    parser.parse_file("test.pacman")
    
    installer = Installer(parser.packages)
    installer._install_packages()