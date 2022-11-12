import pandas

def load_table():
    PubVPN_URL = "http://www.vpngate.net/api/iphone/"
    Source = pandas.read_csv(PubVPN_URL, header=1)
    Source = Source[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]
    print(Source.head(10)) # List the first 10 rows of the PublicVPN list
    print('\n---------------------\n')
