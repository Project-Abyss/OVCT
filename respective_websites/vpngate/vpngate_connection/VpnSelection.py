import pandas as pd
import csv, base64

def selectOne(Source, Show_List):
    list_file = Source
    if Show_List == "y":
        print('\n-----------------------------------\n\n【 Public VPN 10 filtered records 】\n')
        print(list_file[['#HostName', 'CountryLong', 'IP', 'Speed']].head(10))
        print('\n-----------------------------------\n')
    else:
        pass
        
    vpn_hostname = input("【 Please input VPN ISP hostname 】\n\n=> ")

    while(vpn_hostname not in list(list_file['#HostName'])):
        print("\n[Sorry, this Hostname isn't in the all_resources.csv, please input again.]")
        print('\n-----------------------------------\n')
        vpn_hostname = input("【 Please input VPN ISP hostname 】\n\n=> ")        
    
    print('\n-----------------------------------\n')

    filter = list_file['#HostName'] == vpn_hostname
    vpn_data = list_file[(filter)].values.tolist()[0]
    vpn_ip = vpn_data[2]
    vpn_country = vpn_data[1]
    if " " in vpn_country:
        vpn_country = vpn_country.replace(" ", "_")
    else:
        pass
    return vpn_hostname, vpn_ip, vpn_country

def decodeSelectedVpn(Filtered_Csv_Path, Vpn_Hostname):
    list_file = pd.read_csv(Filtered_Csv_Path)
    filter = list_file['#HostName'] == Vpn_Hostname
    vpn_data = list_file[(filter)]

    base64_message = str(vpn_data['OpenVPN_ConfigData_Base64'].values)
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    ovpn_file_content = message_bytes.decode('ascii')

    return ovpn_file_content
