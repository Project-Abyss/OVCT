import pandas as pd
import csv, base64
from functions import webcrawler

def list_reload(Updated_Source, All_Source_Path):
    Updated_Source.to_csv(All_Source_Path, sep=',', index=False)

def save_file(Filtered_Source, Folder_Path):
    print('\n-----------------------------------\n')
    file_name = input("【 Please input the CSV file name that you want to save. 】 \n\nPlease enter the file name\n\n=> ")
    Path = Folder_Path + file_name +'.csv'
    Filtered_Source.to_csv(Path, sep=',', index=False)
    print("\n[ The reslut has been saved in {}.csv ]\n".format(file_name))
    return Path

def append_new_list(All_Source_Path):
    old_list = pd.read_csv(All_Source_Path)
    new_list = webcrawler.load_table()
    update_list = old_list.merge(new_list, how='outer', indicator=True).loc[lambda x : x['_merge'] == 'right_only']
    update_list = update_list.drop(["_merge"], axis=1)
    update_list.to_csv(All_Source_Path, mode = 'a', header = False, index = False)
