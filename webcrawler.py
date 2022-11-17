import pandas

def load_table():
    print('-------------------------------------------------------------\n')
    # selection = input("【 Please enter the number for selecting resource. 】\n\n1. Update public VPN list from `vpngate website` right now. \n2. Use the provided public VPN list. (Default) \n\n=> ")

    # if selection == "1":

    PubVPN_URL = "http://www.vpngate.net/api/iphone/"
    Source = pandas.read_csv(PubVPN_URL, header=1)
    Source['Speed'] = Source['Speed'] / 1000000
    Source = Source[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]
    print("The publicVPN have been updated.")
    return Source