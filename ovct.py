import os, sys
import configparser as cp
inifile_name = "./config.ini"
inifile = cp.ConfigParser()
inifile.read(inifile_name, 'UTF-8')

from load_module import *

if __name__ == "__main__":
    loading()
    
    Updated_Source = initialize.get_current_list(inifile["File_Path"]["all_resources"])
    menu.choose_operation(Updated_Source, inifile["File_Path"]["all_resources"], inifile["File_Path"]["resources"])
