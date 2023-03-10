import pandas
import csv
from functions import vpnselection, decode, connection, file_storage

def filter(result):
    Input_Country = " "
    print('\n-----------------------------------\n')
    selection = input("【 Please enter the number for selecting one of the criteria to filter. 】\n\n1. Country \n2. Speed \n3. Country & Speed \n\n=> ")

    # Enter 1: country
    if selection == "1":
        result = filter_country(result)
        ask_save_or_not(result)
        ask_connection_or_not(result)

    # Enter 2: speed
    elif selection == "2":
        result = filter_speed(result, Input_Country)
        ask_save_or_not(result)
        ask_connection_or_not(result)

    # Enter 3: country & speed
    elif selection == "3":
        result = filter_country(result)
        result = filter_speed(result, Input_Country)
        ask_save_or_not(result)
        ask_connection_or_not(result)
    
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

def filter_speed(Source, Input_Country):
    Speed_list = Source.filter(items=['Speed'])
    SpeedMax = Speed_list.max()  
    SpeedMin = Speed_list.min()
    print('\n-----------------------------------\n')
    print('The Speed Range: ' + SpeedMin.to_string(index=False) + ' Mbps' + ' ~ ' + SpeedMax.to_string(index=False) + ' Mbps')
    Speed = int(input("\n【 How fast the VPN would you prefer 】\n\n=> "))
    
    Source = Source.query('Speed >= {}'.format(Speed))
    return Source

def no_filter(Source):
    return Source

def ask_connection_or_not(Source):
    Connection_or_not = input("【 Do you want to connection vpn now?(Y/N) 】 \n\n=> ")
    if Connection_or_not == "Y" or Connection_or_not == "y":
        print('\n-----------------------------------\n')
        vpn_hostname, vpn_ip, vpn_country = vpnselection.select_one(filtered_csv_path = "./resources/all_resources.csv", show_list = "n")
        ovpn_file_content = decode.vpn("./resources/all_resources.csv", vpn_hostname)
        connection.system_identify(vpn_hostname, vpn_ip, vpn_country, ovpn_file_content)
    else:
        pass

def ask_save_or_not(Source):
    print('\n-----------------------------------\n')
    Save_or_not = input("【 Save as another list.(Y/N) 】 \n\n=> ")
    if Save_or_not == "Y" or Save_or_not == "y":
        file_storage.save_file(Source)
    else:
        pass
    print('\n-----------------------------------\n\n【 Public VPN 10 filtered records 】\n')
    print(Source[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10))
    print('\n-----------------------------------\n')
