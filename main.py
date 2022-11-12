import platform
import webcrawler
import vpnfilter
import selectvpn
import decode
import connection

if __name__ == "__main__":
    result = webcrawler.load_table()
    filtered_result = vpnfilter.filter(result)
    vpn_hostname = vpnselection.select_one(filtered_result)
    ovpn_file_path = decode.vpn(vpn_hostname)

    if platform.system() == "Linux":
	connection.ubuntu(ovpn_file_path)
    elif platform.system() == "Darwin":
	connection.macos(ovpn_file_path)
    elif platform.system() == "Windows":
	connection.windows(ovpn_file_path)
    else:
        print("Sorry, your operating system is not supported!")
