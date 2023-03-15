import pandas
import csv
from functions import vpnselection, connection, data_processing

class choose_filter_way:
    def filter(All_Source_Path, Folder_Path):
        Source = pandas.read_csv(All_Source_Path)
        Input_Country = " "
        print('\n-----------------------------------\n')
        selection = input("【 Please enter the number for selecting one of the criteria to filter. 】\n\n1. Country \n2. Speed \n3. Country & Speeds \n\n=> ")

        # Enter 1: country
        if selection == "1":
            Filtered_Source = choose_filter_way.filter_country(Source)
            ask_save_or_not(Filtered_Source, Folder_Path)
            ask_connection_or_not(Filtered_Source, All_Source_Path)

        # Enter 2: speed
        elif selection == "2":
            Filtered_Source = choose_filter_way.filter_speed(Source)
            ask_save_or_not(Filtered_Source, Folder_Path)
            ask_connection_or_not(Filtered_Source, All_Source_Path)

        # Enter 3: country & speed
        elif selection == "3":
            Filtered_Source = choose_filter_way.filter_country(Source)
            Filtered_Source = choose_filter_way.filter_speed(Filtered_Source)
            ask_save_or_not(Filtered_Source, Folder_Path)
            ask_connection_or_not(Filtered_Source, All_Source_Path)
            
        else:
            pass
            
    def filter_country(Source):
        Country_list = Source.filter(items=['CountryLong'])
        Country_list = Country_list.astype(str)
        Country_list = Country_list['CountryLong'].values.tolist()
        Country_Set = set(Country_list)
        Country_Set.remove('nan')

        while(True):
            print('\n-----------------------------------\n')
            print('There are some countries you can choose: \n')
            for c in Country_Set:
                print(c.replace(',', ''))
            Input_Country = input("\n\n【 Please enter the country 】 \n\n=> ")
            if (Input_Country in Country_Set):
                break
            else:
                print('\n[Your input is not in the list, please enter it again.]')
                
        Source = Source[Source.CountryLong.eq(Input_Country)]
        return Source

    def filter_speed(Source):
        Speed_list = Source.filter(items=['Speed'])
        SpeedMax = Speed_list.max()  
        SpeedMin = Speed_list.min()
        print('\n-----------------------------------\n')
        print('The Speed Range: ' + SpeedMin.to_string(index=False) + ' Mbps' + ' ~ ' + SpeedMax.to_string(index=False) + ' Mbps')
        Speed = int(input("\n【 How fast the VPN would you prefer 】\n\n=> "))
        
        Source = Source.query('Speed >= {}'.format(Speed))
        return Source

def ask_save_or_not(Filtered_Source, Folder_Path):
    print('\n-----------------------------------\n')
    Save_or_not = input("【 Save as another list.(Y/N) 】 \n\n=> ")
    if Save_or_not == "Y" or Save_or_not == "y":
        data_processing.save_file(Filtered_Source, Folder_Path)
    else:
        pass
    print('\n-----------------------------------\n\n【 Public VPN 10 filtered records 】\n')
    print(Filtered_Source[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10))
    print('\n-----------------------------------\n')

def ask_connection_or_not(Filtered_Source, All_Source_Path):
    Connection_or_not = input("【 Do you want to connection vpn now?(Y/N) 】 \n\n=> ")
    if Connection_or_not == "Y" or Connection_or_not == "y":
        print('\n-----------------------------------\n')
        vpn_hostname, vpn_ip, vpn_country = vpnselection.select_one(Filtered_Source, show_list = "n")
        ovpn_file_content = vpnselection.decode_selected_vpn(All_Source_Path, vpn_hostname)
        connection.system_identify(vpn_hostname, vpn_ip, vpn_country, ovpn_file_content)
    else:
        pass
