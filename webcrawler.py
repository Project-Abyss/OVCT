import pandas

def load_table():
    selection = input("Please enter the number for selecting resource.\n1. Update public VPN list from `vpngate website` right now \t2. Use the provided public VPN list (Default) \n\n=> ")

    if selection == "1":
        PubVPN_URL = "http://www.vpngate.net/api/iphone/"
        Source = pandas.read_csv(PubVPN_URL, header=1)
        Source = Source[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]
    else:
        Source = pandas.read_csv("PublicVPN_List.csv")

    print(Source.head(10)) # List the first 10 rows of the PublicVPN list
    print('\n---------------------\n')
    return Source
