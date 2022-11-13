import pandas 
import csv

def select_one(filtered_csv_path):

    list_file = pandas.read_csv(filtered_csv_path)
    print(list_file)

    vpn_hostname = input("Please input VPN ISP hostname: \n\n=> ")

    while(vpn_hostname not in list(list_file['#HostName'])):
        vpn_hostname = input("Please input VPN ISP hostname: \n\n=> ")
        print("\n[Sorry, this Hostname isn't in the PublicVPN_list.csv, please input again.]\n")
    
    print('\n---------------------\n')

    filter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(filter)].values.tolist()[0]
    vpn_ip = VPN_data[2]
    vpn_country = VPN_data[1]
    if " " in vpn_country:
        vpn_country = vpn_country.replace(" ", "_")
    else:
        pass
    return vpn_hostname, vpn_ip, vpn_country
