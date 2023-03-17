import pandas
import csv
from shared_functions import DataProcessing
from respective_websites.vpngate.vpngate_connection import VpnSelection, Connection

class ChooseFilterWay:
    def filter(Folder_Path, File_Name):
        File_Path = Folder_Path + File_Name +'.csv'
        source = pandas.read_csv(File_Path)
        print('\n-----------------------------------\n')
        selection = input("【 Please enter the number for selecting one of the criteria to filter. 】\n\n1. Country \n2. Speed \n3. Country & Speeds \n\n=> ")

        # Enter 1: country
        if selection == "1":
            Filtered_source = ChooseFilterWay.filterCountry(source)
            askSaveOrNot(Filtered_source, Folder_Path)
            askConnectionOrNot(Filtered_source, File_Path)

        # Enter 2: speed
        elif selection == "2":
            Filtered_source = ChooseFilterWay.filterSpeed(source)
            askSaveOrNot(Filtered_source, Folder_Path)
            askConnectionOrNot(Filtered_source, File_Path)

        # Enter 3: country & speed
        elif selection == "3":
            Filtered_source = ChooseFilterWay.filterCountry(source)
            Filtered_source = ChooseFilterWay.filterSpeed(Filtered_source)
            askSaveOrNot(Filtered_source, Folder_Path)
            askConnectionOrNot(Filtered_source, File_Path)
            
        else:
            pass
            
    def filterCountry(source):
        country_list = source.filter(items=['CountryLong'])
        country_list = country_list.astype(str)
        country_list = country_list['CountryLong'].values.tolist()
        country_set = set(country_list)
        country_set.remove('nan')

        while(True):
            print('\n-----------------------------------\n')
            print('There are some countries you can choose: \n')
            for c in country_set:
                print(c.replace(',', ''))
            input_country = input("\n\n【 Please enter the country 】 \n\n=> ")
            if (input_country in country_set):
                break
            else:
                print('\n[Your input is not in the list, please enter it again.]')
                
        source = source[source.CountryLong.eq(input_country)]
        return source

    def filterSpeed(source):
        speed_list = source.filter(items=['Speed'])
        speedmax = speed_list.max()  
        speedmin = speed_list.min()
        print('\n-----------------------------------\n')
        print('The Speed Range: ' + speedmin.to_string(index=False) + ' Mbps' + ' ~ ' + speedmax.to_string(index=False) + ' Mbps')
        speed = int(input("\n【 How fast the VPN would you prefer 】\n\n=> "))
        
        source = source.query('Speed >= {}'.format(speed))
        return source

def askSaveOrNot(Filtered_source, Folder_Path):
    print('\n-----------------------------------\n')
    save_or_not = input("【 Save as another list.(Y/N) 】 \n\n=> ")
    if save_or_not == "Y" or save_or_not == "y":
        DataProcessing.saveFile(Filtered_source, Folder_Path)
    else:
        pass
    print('\n-----------------------------------\n\n【 Public VPN 10 filtered records 】\n')
    print(Filtered_source[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10))
    print('\n-----------------------------------\n')

def askConnectionOrNot(Filtered_source, File_Path):
    connection_or_not = input("【 Do you want to connection vpn now?(Y/N) 】 \n\n=> ")
    if connection_or_not == "Y" or connection_or_not == "y":
        print('\n-----------------------------------\n')
        vpn_hostname, vpn_ip, vpn_country = VpnSelection.selectOne(Filtered_source, show_list = "n")
        ovpn_file_content = VpnSelection.decodeSelectedVpn(File_Path, vpn_hostname)
        Connection.systemIdentify(vpn_hostname, vpn_ip, vpn_country, ovpn_file_content)
    else:
        pass
