import os, sys

import set_init
set_init.init_file_name()
from functions import *

import configparser as cp
inifile_name = "./config.ini"
inifile = cp.ConfigParser()
inifile.read(inifile_name, 'UTF-8')

if __name__ == "__main__":
    set_init.init_file_name()

    Updated_Source = initialize.get_current_list(inifile["File_Path"]["all_resources"])
    menu.choose_operation(Updated_Source, inifile["File_Path"]["all_resources"], inifile["File_Path"]["resources"])
