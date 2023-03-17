import os, sys
import pandas as pd

from shared_functions import WebsiteFunction


def chooseOperation(Folder_Path, File_Name, Website_Name):
    while(True):
        file_path = Folder_Path + File_Name +'.csv'
        source = pd.read_csv(file_path)
        print("\n======================================================================\n\n【 Public VPN 10 records 】\n")
        print(source[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10)) # List the first 10 rows of the PublicVPN list
        print('\n======================================================================\n')

        function_chioce = input("Choose a Function: \n\n 1. Update the public VPN list \n 2. Filter the public VPN list \n 3. Connection \n 0. Exit\n\n=> ")
        
        if function_chioce == '1':
            if Website_Name == 'vpngate':
                WebsiteFunction.Vpngate.update(file_path)

        elif function_chioce == '2':
            if Website_Name == 'vpngate':
                WebsiteFunction.Vpngate.filter(Folder_Path, File_Name)

        elif function_chioce == '3':
            print('\n-----------------------------------\n')
            print('You can enter a csv file name of these...\n')
            for i in range(len(os.listdir(Folder_Path))):
                if os.listdir(Folder_Path)[i].endswith(".csv"):
                    print(os.listdir(Folder_Path)[i].replace('.csv', ''))
            print('\n-----------------------------------\n')
            
            selected_file_name = input("【 Please enter the VPN list name 】\n\n=> ")
            filtered_csv_path = Folder_Path + selected_file_name + ".csv"
            while (filtered_csv_path.strip() == '') or (os.path.exists(filtered_csv_path) == False):
                print("\n[Sorry, this path information is necessary, please input again.]")
                print('\n-----------------------------------\n')
                selected_file_name = input("【 Please enter the VPN list name 】\n\n=> ")
                filtered_csv_path = Folder_Path + selected_file_name + ".csv"
            source = pd.read_csv(filtered_csv_path)

            if Website_Name == 'vpngate':
                WebsiteFunction.Vpngate.connection(source, filtered_csv_path)
        
        elif function_chioce == '0':
            sys.exit()

        else:
            pass
