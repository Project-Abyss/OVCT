import base64

def vpn(vpn_hostname):

    fliter = list_file['#HostName'] == vpn_hostname
    VPN_data = list_file[(fliter)]

    base64_message = str(VPN_data['OpenVPN_ConfigData_Base64'].values)
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    ovpn_file_path = message_bytes.decode('ascii')

    return ovpn_file_path
