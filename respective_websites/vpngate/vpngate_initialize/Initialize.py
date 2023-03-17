import WebCrawler
import configparser as cp
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from shared_functions import DataProcessing

inifile_name = "../../../config.ini"
inifile = cp.ConfigParser()
inifile.read(inifile_name, 'UTF-8')

print("\n[ Initializing... ]")
updated_source = WebCrawler.loadTable()
file_path = '../../../' + inifile["file_path"]["resources"] + inifile["file_path"]["all_resources_name"]
print(file_path)
DataProcessing.listReload(updated_source, file_path)
