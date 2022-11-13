import platform
import webcrawler
import vpnfilter
import vpnselection
import decode
import connection

if __name__ == "__main__":
    result = webcrawler.load_table()
    filtered_csv_path = vpnfilter.filter(result)
    vpn_hostname, vpn_ip, vpn_country = vpnselection.select_one(filtered_csv_path)
    ovpn_file_content = decode.vpn(filtered_csv_path, vpn_hostname)

    if platform.system() == "Linux":
        connection.ubuntu(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
    elif platform.system() == "Darwin":
        connection.macos(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
    elif platform.system() == "Windows":
        connection.windows(ovpn_file_content, vpn_hostname, vpn_ip, vpn_country)
    else:
        print("Sorry, your operating system is not supported!")
