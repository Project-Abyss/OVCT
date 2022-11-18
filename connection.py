import re
import os
import sys

def ubuntu(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):

    openvpn_path = input("【 Please input your openVPN software file path. 】\n\n E.g. /etc/openvpn \n\n=> ")
    while(openvpn_path.strip() == ''):
        print("[Sorry, this path information is necessary, please input again.]")
        print('\n-----------------------------------\n')
        openvpn_path = input("【 Please input your openVPN software file path. 】\n\n E.g. /etc/openvpn \n\n=> ")
    
    print('\n-----------------------------------\n')
    L_path = os.path.join(openvpn_path, 'client', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
    L_path = re.sub("\[|\]|\'","",L_path)
    with open(L_path, mode="w") as file:
        file.write(ovpn_file_content)
    print("\n===== ## Now, the public VPN (Country: {}, Hostname: {}, IP: {}) is connecting. ===== \n\n".format(vpn_country, vpn_hostname, vpn_ip))
    os.system('sudo openvpn --config {}'.format(L_path))


def macos(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):

    ovpn_file_path = os.path.join(os.getcwd(), 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
    with open(ovpn_file_path, mode="w") as file:
        file.write(ovpn_file_content)
    os.system("/Applications/OpenVPN\ Connect/OpenVPN\ Connect.app/Contents/MacOS/OpenVPN\ Connect --import-profile={}".format(ovpn_file_path))
    print("\n## The vpngate_{}_{}_{}.ovpn file imported successfully. \n\n===== ## Now, you can connect with OpenVPN ! ===== \n\n".format(vpn_hostname, vpn_country, vpn_ip)) 

def windows(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):

    openvpn_path = input("【 Please input your openVPN software file path. 】\n\n E.g. /etc/openvpn \n\n=> ")    
    while(openvpn_path.strip()==''): 
        print("\n[Sorry, this path information is necessary, please input again.]")
        print('\n-----------------------------------\n')
        openvpn_path = input("【 Please input your openVPN software file path. 】\n\n E.g. /etc/openvpn \n\n=> ")

    print('\n-----------------------------------\n')
    W_path = os.path.join(openvpn_path, 'config', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
    with open(W_path, mode="w") as file:
        file.write(ovpn_file_content)
    print("\n## The vpngate_{}_{}_{}.ovpn file imported successfully. \n\n===== ## Now, you can connect with OpenVPN ! ===== \n\n".format(vpn_hostname, vpn_country, vpn_ip))
