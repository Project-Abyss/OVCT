import re
import os
import sys

def ubuntu(ovpn_file_path, vpn_hostname):
    
    list_file = pandas.read_csv(filtered_result)
    fliter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(fliter)]
    IP = str(VPN_data['IP'].values)
    Country = str(VPN_data['CountryLong'].values)

    characters = "'[] "
    for x in range(len(characters)):
        Country = Country.replace(characters[x],"")
        IP = IP.replace(characters[x],"")

    openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    
    while(openvpn_path.strip() == ''): 
        print("\n[Sorry, this path information is necessary, please input again.]\n")
        print('\n---------------------\n')
        openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    print('\n---------------------\n')

    W_path = os.path.join(openvpn_path, 'config', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, Country, IP))
    with open(W_path, mode="w") as file:
        file.write(ovpn_file_path)
    print("\n[ The \"vpngate_{}_{}_{}.ovpn\"".format(vpn_hostname, Country, IP), "file import complete! ]")


def macos(ovpn_file_path, vpn_hostname):

    list_file = pandas.read_csv(filtered_result)
    fliter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(fliter)]
    IP = str(VPN_data['IP'].values)
    Country = str(VPN_data['CountryLong'].values)

    characters = "'[] "
    for x in range(len(chaacters)):
        Country = Country.replace(characters[x],"")
        IP = IP.replace(characters[x],"")

    ovpn_file_path = os.path.join(os.getcwd(), 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, Country, IP))
    with open(ovpn_file_path, mode="w") as file:
        file.write(ovpn_file_path)
    os.system("/Applications/OpenVPN\ Connect/OpenVPN\ Connect.app/Contents/MacOS/OpenVPN\ Connect --import-profile={}".format(ovpn_file_path))
    print("\n=> The vpngate_{}_{}_{}.ovpn file imported successfully.".format(vpn_hostname, Country, IP)) 
 

def windows(ovpn_file_path, vpn_hostname):
    
    list_file = pandas.read_csv(filtered_result)
    fliter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(fliter)]
    IP = str(VPN_data['IP'].values)
    Country = str(VPN_data['CountryLong'].values)

    characters = "'[] "
    for x in range(len(chaacters)):
        Country = Country.replace(characters[x],"")
        IP = IP.replace(characters[x],"")
    
    openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    
    while(openvpn_path.strip()==''): 
        print("\n[Sorry, this path information is necessary, please input again.]\n")
        print('\n---------------------\n')
        openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    print('\n---------------------\n')

    W_path = os.path.join(openvpn_path, 'config', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, Country, IP))
    with open(W_path, mode="w") as file:
        file.write(ovpn_file_path)
    print("\n[ The \"vpngate_{}_{}_{}.ovpn\"".format(vpn_hostname, Country, IP), "file import complete! ]")
