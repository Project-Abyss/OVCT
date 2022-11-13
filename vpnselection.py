import pandas 
import csv

def select_one(filtered_result):

    list_file = pandas.read_csv(filtered_result)
    vpn_hostname = input("Please input VPN ISP hostname: \n\n=> ")

    while(vpn_hostname not in list(list_file['#HostName'])):

        vpn_hostname = input("Please input VPN ISP hostname: \n\n=> ")
        print("\n[Sorry, this Hostname isn't in the PublicVPN_list.csv, please input again.]\n")
    
    print('\n---------------------\n')
    return vpn_hostname  
