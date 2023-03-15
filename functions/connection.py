import re, os, sys, platform

def system_identify(vpn_hostname, vpn_ip, vpn_country, ovpn_file_content):
    if platform.system() == "Linux":
        ovpn_file_path = file_generate.ubuntu(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
        connection.ubuntu(ovpn_file_path)
    elif platform.system() == "Darwin":
        ovpn_file_path = file_generate.macos(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
        connection.macos(ovpn_file_path)
    elif platform.system() == "Windows":
        windows(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
    else:
        print("Sorry, your operating system is not supported!")
        sys.exit()
    sys.exit()
    
class file_generate:
    def ubuntu(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):
        openvpn_path = "/etc/openvpn"
        ovpn_file_path = os.path.join(openvpn_path, 'client', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
        ovpn_file_path = re.sub("\[|\]|\'","",ovpn_file_path)
        with open(ovpn_file_path, mode="w") as file:
            file.write(ovpn_file_content)
        print("\n===== ## Now, the public VPN (Country: {}, Hostname: {}, IP: {}) is connecting. ===== \n\n".format(vpn_country, vpn_hostname, vpn_ip))
        return ovpn_file_path

    def macos(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):
        ovpn_file_path = os.path.join(os.getcwd(), 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
        with open(ovpn_file_path, mode="w") as file:
            file.write(ovpn_file_content)
        print("\n## The vpngate_{}_{}_{}.ovpn file imported successfully. \n\n===== ## Now, you can connect with OpenVPN ! ===== \n\n".format(vpn_hostname, vpn_country, vpn_ip)) 
        return ovpn_file_path

    def windows(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country):
        openvpn_path = input("【 Please input your openVPN software file path. 】\n\n E.g. /etc/openvpn \n\n=> ")    
        while(openvpn_path.strip()==''): 
            print("\n[Sorry, this path information is necessary, please input again.]")
            print('\n-----------------------------------\n')
            openvpn_path = input("【 Please input your openVPN software file path. 】\n\n E.g. /etc/openvpn \n\n=> ")

        print('\n-----------------------------------\n')
        ovpn_file_path = os.path.join(openvpn_path, 'config', 'vpngate_{}_{}_{}.ovpn'.format(vpn_hostname, vpn_country, vpn_ip))
        with open(ovpn_file_path, mode="w") as file:
            file.write(ovpn_file_content)
        print("\n## The vpngate_{}_{}_{}.ovpn file imported successfully. \n\n===== ## Now, you can connect with OpenVPN ! ===== \n\n".format(vpn_hostname, vpn_country, vpn_ip))

class connection:
    def ubuntu(ovpn_file_path):
        os.system('sudo openvpn --config {}'.format(ovpn_file_path))
    def macos(ovpn_file_path):
        os.system("/Applications/OpenVPN\ Connect/OpenVPN\ Connect.app/Contents/MacOS/OpenVPN\ Connect --import-profile={}".format(ovpn_file_path))
