import time 
import colorama
from colorama import Fore, Back, Style
colorama.init()
import xml.dom.minidom as mdom
import os.path
from os.path import exists
from os import path

opt = Back.WHITE + Fore.BLACK
default = Back.BLACK + Fore.WHITE

from configparser import ConfigParser

def path():
    config = ConfigParser()
    path_user = str(input("Payday2's (renderer_settings.xml) Directory: "))
    path_user = path_user + "\\renderer_settings.xml"
    config["Payday2Fixer"] = {
        "path": path_user,
        "endvalue": 1
    }
    with open('config.ini', 'w') as f:
        config.write(f)


def adapterindex_one():
    config.read("config.ini")
    config_data = config["Payday2Fixer"]
    
    with open(config_data["path"], 'r') as file:
        content = file.read()
    content = content.replace(f'adapter_index = "0"', f'adapter_index = "1"')

    with open(config_data["path"], 'w+') as file:
        file.write(content)
    main()


def adapterindex_zero():
    config.read("config.ini")
    config_data = config["Payday2Fixer"]

    with open(config_data["path"], 'r') as file:
        content = file.read()
    content = content.replace(f'adapter_index = "1"', f'adapter_index = "0"')

    with open(config_data["path"], 'w+') as file:
        file.write(content)
    main()

def check_adapter():
    config.read("config.ini")
    config_data = config["Payday2Fixer"]
    with open(config_data["path"], 'r') as file:
        for line in file:
            if 'adapter_index = "0"' in line:
                print('- adapter_index = "0", setting it to "1"')
                adapterindex_one()
            elif 'adapter_index = "1"' in line:
                print('- adapter_index = "1", setting it to "0".')
                adapterindex_zero()

def main():
    print(opt + "Payday2 Fixer")
    print(default + "Select an option.")
    print(opt + "| 1.Adapter Index |" + default)

    while True:
        user_choice = str(input("> "))

        match user_choice:
            case '1':
                check_adapter()
                break
    

if __name__ == '__main__':
    config = ConfigParser()
    verification = exists('config.ini')
    if verification == False: 
        path()
    elif verification == True:
        main()