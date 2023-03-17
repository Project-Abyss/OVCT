import pandas

def loadTable():

    print('-------------------------------------------------------------\n')

    vpngate_url = "http://www.vpngate.net/api/iphone/"
    source = pandas.read_csv(vpngate_url, header=1)
    source['Speed'] = source['Speed'] / 1000000
    source = source[['#HostName', 'CountryLong', 'IP', 'Speed', 'OpenVPN_ConfigData_Base64']]
    return source
