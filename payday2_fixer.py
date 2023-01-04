import time 
import colorama
from colorama import Fore, Back, Style
colorama.init()
import xml.dom.minidom as mdom
import xml.etree.ElementTree as ET
import os.path
from os.path import exists
from os import path

opt = Back.WHITE + Fore.BLACK
default = Back.BLACK + Fore.WHITE

from configparser import ConfigParser

resolution_save = None
ratio_save = None
width = 0
height = 0

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


def change_resolution():
    global width, height
    global resolution_save
    config.read("config.ini")
    config_data = config["Payday2Fixer"]
    with open(config_data["path"], 'r') as file:
        new_resolution = file.read()
    width = str(input("New width: "))
    height = str(input("New height: "))
    int(width)
    int(height)
    newest_resolution = f'        resolution = "{width} {height}"\n'
    new_resolution = new_resolution.replace(resolution_save, newest_resolution)

    with open(config_data["path"], 'w+') as file:
        file.write(new_resolution)
    aspect_ratio()

def aspect_ratio():
    global width, height
    global ratio_save
    config.read("config.ini")
    config_data = config["Payday2Fixer"]

    with open(config_data["path"],'r') as f:
        for lines in f:
            lines.strip()
            if "aspect_ratio" in lines:
                resolution_save = lines
                print("Current aspect_ratio:",lines) 
                ratio_save = lines
                break

    with open(config_data["path"], 'r') as file:
        aspect = file.read()
    ratio = int(width)/int(height)
    print("New aspect_ratio:", ratio)
    newest_ratio = f'        aspect_ratio = "{ratio}"\n'
    aspect = aspect.replace(ratio_save, newest_ratio)

    with open(config_data["path"], 'w+') as file:
        file.write(aspect)
    main()

def check_resolution():
    global resolution_save
    config.read("config.ini")
    config_data = config["Payday2Fixer"]
    with open(config_data["path"],'r') as f:
        for lines in f:
            lines.strip()
            if "resolution" in lines:
                resolution_save = lines
                print("Current resolution:",lines) 
                change_resolution()
                break

def main():
    print(opt + "Payday2 Fixer")
    print(default + "Select an option.")
    print(opt + "| 1.Adapter Index |  | 2.Resolution |" + default)

    while True:
        user_choice = str(input("> "))

        match user_choice:
            case '1':
                check_adapter()
                break
            case '2':
                check_resolution()
                break

    

if __name__ == '__main__':
    config = ConfigParser()
    verification = exists('config.ini')
    if verification == False: 
        path()
    elif verification == True:
        main()