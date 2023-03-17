import pandas as pd
import csv, base64

from respective_websites.vpngate.vpngate_initialize import Webcrawler

def listReload(Updated_Source, All_Source_Path):
    Updated_Source.to_csv(All_Source_Path, sep=',', index=False)
    print("[ The publicVPN have been updated! ]")

def saveFile(Filtered_Source, Folder_Path):
    print('\n-----------------------------------\n')
    file_name = input("【 Please input the CSV file name that you want to save. 】 \n\nPlease enter the file name\n\n=> ")
    path = Folder_Path + file_name +'.csv'
    Filtered_Source.to_csv(path, sep=',', index=False)
    print("\n[ The reslut has been saved in {}.csv ]\n".format(file_name))
    return path

def appendNewList(File_Path):
    old_list = pd.read_csv(File_Path)
    new_list = Webcrawler.loadTable()
    update_list = old_list.merge(new_list, how='outer', indicator=True).loc[lambda x : x['_merge'] == 'right_only']
    update_list = update_list.drop(["_merge"], axis=1)
    update_list.to_csv(File_Path, mode = 'a', header = False, index = False)
    print("[ The publicVPN have been updated! ]")
