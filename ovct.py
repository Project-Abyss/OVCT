import os, sys
import configparser as cp
from shared_functions import Menu

if __name__ == "__main__":
    inifile_name = "./config.ini"
    inifile = cp.ConfigParser()
    inifile.read(inifile_name, 'UTF-8')
    Menu.chooseOperation(inifile["file_path"]["resources"], inifile["file_path"]["vpngate_resources_name"], inifile["website_info"]["website_name"])
