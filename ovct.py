import os, sys
import configparser as cp
from import_functions import *

if __name__ == "__main__":
    loading()
    inifile_name = "./config.ini"
    inifile = cp.ConfigParser()
    inifile.read(inifile_name, 'UTF-8')
    Updated_Source = initialize.get_current_list(inifile["File_Path"]["all_resources"])
    menu.choose_operation(Updated_Source, inifile["File_Path"]["all_resources"], inifile["File_Path"]["resources"])
