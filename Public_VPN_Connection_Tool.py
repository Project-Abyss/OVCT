import re
import os
import sys
import base64
import platform
import pandas 
import csv

def CountryFilter(Source):
    Country_list = Source.filter(items=['CountryLong'])
    Country_list = Country_list.astype(str)
    Country_list = Country_list['CountryLong'].values.tolist()
    Country_Set = set(Country_list)
    Country_Set.remove('nan')
    while(True):
        print('There are some countries you can choose: ')
        print(Country_Set)
        Input_Country = input("Please enter the country: \n\n=> ")
        print('\n---------------------\n')
        if(Input_Country in Country_Set):
            break
        else:
            print('Your input is not in the list, please enter it again.')
    Source = Source[Source.CountryLong.eq(Input_Country)]
    return Source

def SpeedFilter(Source):
    Speed_list = Source.filter(items=['Speed'])
    SpeedMax = Speed_list.max()
    SpeedMax /= 1000000    
    SpeedMin = Speed_list.min()
    SpeedMin /= 1000000
    print('The Speed Range: ' + SpeedMin.to_string(index=False) + ' Mbps' + ' ~ ' + SpeedMax.to_string(index=False) + ' Mbps')
    Speed = int(input("How fast the VPN would you prefer: \n\n=> "))
    print('\n---------------------\n')
    Speed *= 1000000
    Source = Source.query('Speed >= {}'.format(Speed))
    return Source

def Export(Source):
    Path = input("Where would you like to save the CSV file (Please enter the absolute path and the \"file name\" (E.g. /home/user/Desktop/[choose a file_name]): \n\n=> ")
    Path += '.csv'
    Source.to_csv(Path, sep=',', index=False)
    print("\n[The result has outputted!]")
    print('\n---------------------\n')


# VPN Data
PubVPN_URL = "http://www.vpngate.net/api/iphone/"
Source = pandas.read_csv(PubVPN_URL, header=1)
Source = Source[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]

# List the first 10 rows of the PublicVPN list
print(Source.head(10))
print('\n---------------------\n')

# Filter function
answer = input('Please select one of the criteria to filter.\n1. Country \t2. Speed \t3. Without filtering (default) \n\n=> ')
print('\n---------------------\n')
if(answer == '1'):
    Source = CountryFilter(Source)
    Export(Source)
elif(answer == '2'):
    Source = SpeedFilter(Source)
    Export(Source)
else:
    Export(Source)

#---------------------------------------------------------------------------------------------
# VPN connect

# User's OS
if platform.system() == "Windows" or "Linux" or "Darwin":
        list_file = pandas.read_csv(Path)
else:
    print("Sorry, this operating system is not supported!")
    os._exit(0)

# PublicVPN_list.csv data
flag = 1
while(flag == 1):
    if platform.system() == "Darwin":
        break
    elif platform.system() == "Windows" or "Linux":
        openvpn_path = input("Please input your openVPN software file path. (E.g. /etc/openvpn): \n\n=> ")
        if openvpn_path.strip()=='': 
            flag = 1
            print("\n[Sorry, this path information is necessary, please input again.]\n")
        else:
            flag = 0
        print('\n---------------------\n')
    else:
        break

flag = 1
while(flag == 1):
    host_name = input("Please input VPN ISP hostname: \n\n=> ")
    if host_name not in list(list_file['#HostName']):
        flag = 1
        print("\n[Sorry, this Hostname isn't in the PublicVPN_list.csv, please input again.]\n")
    else:
        flag = 0
    print('\n---------------------\n')

fliter = list_file['#HostName'] == host_name
VPN_data = list_file[(fliter)]
IP = str(VPN_data['IP'].values)
Country = str(VPN_data['CountryLong'].values)

characters = "'[] "
for x in range(len(characters)):
    Country = Country.replace(characters[x],"")
    IP = IP.replace(characters[x],"")

# Decode base64 to ascii
base64_message = str(VPN_data['OpenVPN_ConfigData_Base64'].values)
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

## Linux ##
if platform.system() == "Linux":
    #print(IP,'/',Country,'\\',message)
    L_path = os.path.join(openvpn_path, 'client', 'vpngate_{}_{}_{}.ovpn'.format(host_name, Country, IP))
    L_path = re.sub("\[|\]|\'","",L_path)
    with open(L_path, mode="w") as file:
        file.write(message)
    os.system('sudo openvpn --config {}'.format(L_path))

## MacOS ##
elif platform.system() == "Darwin":
    ovpn_file_path = os.path.join(os.getcwd(), 'vpngate_{}_{}_{}.ovpn'.format(host_name, Country, IP))
    with open(ovpn_file_path, mode="w") as file:
        file.write(message)
    os.system("/Applications/OpenVPN\ Connect/OpenVPN\ Connect.app/Contents/MacOS/OpenVPN\ Connect --import-profile={}".format(ovpn_file_path))
    print("\n=> The vpngate_{}_{}_{}.ovpn file imported successfully.".format(host_name, Country, IP)) 
 
## Windows ##   
elif platform.system() == "Windows":
    # save .ovpn file
    # file name : vpngate_{Hostname}_{Country}_{IP}.ovpn
    W_path = os.path.join(openvpn_path, 'config', 'vpngate_{}_{}_{}.ovpn'.format(host_name, Country, IP))
    with open(W_path, mode="w") as file:
        file.write(message)
    print("\n[ The \"vpngate_{}_{}_{}.ovpn\"".format(host_name, Country, IP), "file import complete! ]")

else:
    print("Sorry, this operating system is not supported!")
