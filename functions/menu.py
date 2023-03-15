from functions import data_processing, vpnfilter, vpnselection, connection
import os, sys
import pandas as pd

def choose_operation(Updated_Source, All_Source_Path, Folder_Path):
    while(True):
        print("\n======================================================================\n\n【 Public VPN 10 records 】\n")
        print(Updated_Source[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10)) # List the first 10 rows of the PublicVPN list
        print('\n======================================================================\n')

        function_chioce = input("Choose a Function: \n\n 1. Update the public VPN list \n 2. Filter the public VPN list \n 3. Connection \n 0. Exit\n\n=> ")
        
        if function_chioce == '1':
            data_processing.append_new_list(All_Source_Path)

        elif function_chioce == '2':
            vpnfilter.choose_filter_way.filter(All_Source_Path, Folder_Path)

        elif function_chioce == '3':
            print('\n-----------------------------------\n')
            print('You can enter the csv file of these...\n')
            for i in range(len(os.listdir(Folder_Path))):
                if os.listdir(Folder_Path)[i].endswith(".csv"):
                    print(os.listdir(Folder_Path)[i].replace('.csv', ''))
            print('\n-----------------------------------\n')
            
            file_name = input("【 Please enter the VPN list name 】\n\n=> ")
            filtered_csv_path = Folder_Path + file_name + ".csv"
            while (filtered_csv_path.strip() == '') or (os.path.exists(filtered_csv_path) == False):
                print("\n[Sorry, this path information is necessary, please input again.]")
                print('\n-----------------------------------\n')
                file_name = input("【 Please enter the VPN list name 】\n\n=> ")
                filtered_csv_path = Folder_Path + file_name + ".csv"

            Source = pd.read_csv(filtered_csv_path)               
            vpn_hostname, vpn_ip, vpn_country = vpnselection.select_one(Source, show_list = "y")
            ovpn_file_content = vpnselection.decode_selected_vpn(filtered_csv_path, vpn_hostname)
            connection.system_identify(vpn_hostname, vpn_ip, vpn_country, ovpn_file_content)
        
        elif function_chioce == '0':
            sys.exit()

        else:
            pass
