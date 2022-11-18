import pandas
import base64

def vpn(filtered_csv_path, vpn_hostname):

    list_file = pandas.read_csv(filtered_csv_path)
    filter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(filter)]

    base64_message = str(VPN_data['OpenVPN_ConfigData_Base64'].values)
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    ovpn_file_content = message_bytes.decode('ascii')

    return ovpn_file_content
