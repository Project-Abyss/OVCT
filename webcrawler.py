import pandas

def load_table():

    print('-------------------------------------------------------------\n')

    PubVPN_URL = "http://www.vpngate.net/api/iphone/"
    Source = pandas.read_csv(PubVPN_URL, header=1)
    Source['Speed'] = Source['Speed'] / 1000000
    Source = Source[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]
    print("[ The publicVPN have been updated! ]")
    return Source
