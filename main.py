import platform
import pandas
import os
import sys
import webcrawler
import vpnfilter
import vpnselection
import decode
import connection

if __name__ == "__main__":

    result = pandas.read_csv("PublicVPN_List.csv")

    while(True):
    
        print("\n======================================================================\n\n【 Public VPN 10 records 】\n")
        print(result[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10)) # List the first 10 rows of the PublicVPN list
        print('\n======================================================================\n')

        function_chioce = input("Choose a Function: \n\n 1. Update publicVPN list.\n 2. filter the publicVPN list.\n 3. Connection. \n 0. Exit\n\n=>")
        
        if function_chioce == '1':
            result = webcrawler.load_table()

        elif function_chioce == '2':
            filtered_csv_path = vpnfilter.filter(result)
            result = pandas.read_csv(filtered_csv_path)
            #print("read_csv")
            #result = result[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]

        elif function_chioce == '3':
            print('\n-----------------------------------\n')
            filtered_csv_path = input("【 Please enter your VPN list path: 】\n\n=>")
            while(filtered_csv_path.strip() == ''):
                print("[Sorry, this path information is necessary, please input again.]")
                print('\n-----------------------------------\n')
                filtered_csv_path = input("【 Please enter your VPN list path: 】\n\n=> ")
                
            vpn_hostname, vpn_ip, vpn_country = vpnselection.select_one(filtered_csv_path)
            ovpn_file_content = decode.vpn(filtered_csv_path, vpn_hostname)

            if platform.system() == "Linux":
                connection.ubuntu(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
            elif platform.system() == "Darwin":
                connection.macos(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
            elif platform.system() == "Windows":
                connection.windows(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
            else:
                print("Sorry, your operating system is not supported!")
                sys.exit()
        
        elif function_chioce == '0':
            sys.exit()

        else:
            pass

