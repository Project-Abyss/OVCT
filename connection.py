import re
import os
import sys

def ubuntu(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):
    """
    list_file = pandas.read_csv(filtered_result)
    fliter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(fliter)]
    IP = str(VPN_data['IP'].values)
    Country = str(VPN_data['CountryLong'].values)

    characters = "'[] "
    for x in range(len(characters)):
        Country = Country.replace(characters[x],"")
        IP = IP.replace(characters[x],"")
    """
    openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    
    while(openvpn_path.strip() == ''):
        print("\n[Sorry, this path information is necessary, please input again.]\n")
        print('\n---------------------\n')
        openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    print('\n---------------------\n')

    L_path = os.path.join(openvpn_path, 'client', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
    L_path = re.sub("\[|\]|\'","",L_path)
    with open(L_path, mode="w") as file:
        file.write(ovpn_file_content)
    os.system('sudo openvpn --config {}'.format(L_path))


def macos(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):
    """
    list_file = pandas.read_csv(filtered_result)
    fliter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(fliter)]
    IP = str(VPN_data['IP'].values)
    Country = str(VPN_data['CountryLong'].values)

    characters = "'[] "
    for x in range(len(chaacters)):
        Country = Country.replace(characters[x],"")
        IP = IP.replace(characters[x],"")
    """
    ovpn_file_path = os.path.join(os.getcwd(), 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
    with open(ovpn_file_path, mode="w") as file:
        file.write(ovpn_file_content)
    os.system("/Applications/OpenVPN\ Connect/OpenVPN\ Connect.app/Contents/MacOS/OpenVPN\ Connect --import-profile={}".format(ovpn_file_path))
    print("\n=> The vpngate_{}_{}_{}.ovpn file imported successfully.".format(vpn_hostname, vpn_country, vpn_ip)) 
 

def windows(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):
    """
    list_file = pandas.read_csv(filtered_result)
    fliter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(fliter)]
    IP = str(VPN_data['IP'].values)
    Country = str(VPN_data['CountryLong'].values)

    characters = "'[] "
    for x in range(len(chaacters)):
        Country = Country.replace(characters[x],"")
        IP = IP.replace(characters[x],"")
    """
    openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    
    while(openvpn_path.strip()==''): 
        print("\n[Sorry, this path information is necessary, please input again.]\n")
        print('\n---------------------\n')
        openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
    print('\n---------------------\n')

    W_path = os.path.join(openvpn_path, 'config', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
    with open(W_path, mode="w") as file:
        file.write(ovpn_file_content)
    print("\n[ The \"vpngate_{}_{}_{}.ovpn\"".format(vpn_hostname, vpn_country, vpn_ip), "file import complete! ]")
