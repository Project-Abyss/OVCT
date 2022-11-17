import platform
import pandas
import os
import sys
import webcrawler_test
import vpnfilter_test
import vpnselection_test
import decode_test
import connection_test

if __name__ == "__main__":

    result = pandas.read_csv("PublicVPN_List.csv")

    while(True):
    
        print("\n======================================================================\n\n【 Public VPN 10 records 】\n")
        print(result[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10)) # List the first 10 rows of the PublicVPN list
        print('\n======================================================================\n')

        function_chioce = input("Choose a Function: \n\n 1. Update publicVPN list.\n 2. filter the publicVPN list.\n 3. Connection. \n 0. Exit\n\n=>")
        
        if function_chioce == '1':
            result = webcrawler_test.load_table()

        elif function_chioce == '2':
            filtered_csv_path = vpnfilter_test.filter(result)
            result = pandas.read_csv(filtered_csv_path)
            #print("read_csv")
            #result = result[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]

        elif function_chioce == '3':
            print('\n-----------------------------------\n')
            filtered_csv_path = input("Where are your vpn data list: \n\n=>")
            vpn_hostname, vpn_ip, vpn_country = vpnselection_test.select_one(filtered_csv_path)
            ovpn_file_content = decode_test.vpn(filtered_csv_path, vpn_hostname)

            if platform.system() == "Linux":
                connection_test.ubuntu(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
            elif platform.system() == "Darwin":
                connection_test.macos(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
            elif platform.system() == "Windows":
                connection_test.windows(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
            else:
                print("Sorry, your operating system is not supported!")
                sys.exit()
        
        elif function_chioce == '0':
            sys.exit()

        else:
            pass

