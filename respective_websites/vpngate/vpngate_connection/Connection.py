import re, os, sys, platform

def systemIdentify(Vpn_Hostname, Vpn_Ip, Vpn_Country, Ovpn_File_Content):
    if platform.system() == "Linux":
        ovpn_file_path = FileGenerate.Ubuntu(Ovpn_File_Content, Vpn_Hostname, Vpn_Ip, Vpn_Country)
        ConnectionVpn.Ubuntu(ovpn_file_path)
    elif platform.system() == "Darwin":
        ovpn_file_path = FileGenerate.macOS(Ovpn_File_Content, Vpn_Hostname, Vpn_Ip, Vpn_Country)
        ConnectionVpn.macOS(ovpn_file_path)
    elif platform.system() == "Windows":
        FileGenerate.Windows(Ovpn_File_Content, Vpn_Hostname, Vpn_Ip, Vpn_Country)
    else:
        print("Sorry, your operating system is not supported!")
        sys.exit()
    sys.exit()
    
class FileGenerate:
    def Ubuntu(Ovpn_File_Content, Vpn_Hostname, Vpn_Ip, Vpn_Country):
        openvpn_path = "/etc/openvpn"
        ovpn_file_path = os.path.join(openvpn_path, 'client', 'vpngate_{}_{}_{}.ovpn'.format(Vpn_Hostname, Vpn_Country, Vpn_Ip))
        ovpn_file_path = re.sub("\[|\]|\'","",ovpn_file_path)
        with open(ovpn_file_path, mode="w") as file:
            file.write(Ovpn_File_Content)
        print("\n===== ## Now, the public VPN (Country: {}, Hostname: {}, IP: {}) is connecting. ===== \n\n".format(Vpn_Country, Vpn_Hostname, Vpn_Ip))
        return ovpn_file_path

    def macOS(Ovpn_File_Content, Vpn_Hostname, Vpn_Ip, Vpn_Country):
        ovpn_file_path = os.path.join(os.getcwd(), 'vpngate_{}_{}_{}.ovpn'.format(Vpn_Hostname, Vpn_Country, Vpn_Ip))
        with open(ovpn_file_path, mode="w") as file:
            file.write(Ovpn_File_Content)
        print("\n## The vpngate_{}_{}_{}.ovpn file imported successfully. \n\n===== ## Now, you can connect with OpenVPN ! ===== \n\n".format(Vpn_Hostname, Vpn_Country, Vpn_Ip)) 
        return ovpn_file_path

    def Windows(Ovpn_File_Content, Vpn_Hostname, Vpn_Ip, Vpn_Country):
        openvpn_path = input("【 Please input your openVPN software file path. 】\n\n e.g. C:/ProgramFile/openvpn/config \n\n=> ")    
        while(openvpn_path.strip()==''): 
            print("\n[Sorry, this path information is necessary, please input again.]")
            print('\n-----------------------------------\n')
            openvpn_path = input("【 Please input your openVPN software file path. 】\n\n e.g. C:/ProgramFile/openvpn/config \n\n=> ")

        print('\n-----------------------------------\n')
        ovpn_file_path = os.path.join(openvpn_path, 'config', 'vpngate_{}_{}_{}.ovpn'.format(Vpn_Hostname, Vpn_Country, Vpn_Ip))
        with open(ovpn_file_path, mode="w") as file:
            file.write(Ovpn_File_Content)
        print("\n## The vpngate_{}_{}_{}.ovpn file imported successfully. \n\n===== ## Now, you can connect with OpenVPN ! ===== \n\n".format(Vpn_Hostname, Vpn_Country, Vpn_Ip))

class ConnectionVpn:
    def Ubuntu(Ovpn_File_Path):
        os.system('sudo openvpn --config {}'.format(Ovpn_File_Path))
    def macOS(Ovpn_File_Path):
        os.system("/Applications/OpenVPN\ Connect/OpenVPN\ Connect.app/Contents/macOS/OpenVPN\ Connect --import-profile={}".format(Ovpn_File_Path))
