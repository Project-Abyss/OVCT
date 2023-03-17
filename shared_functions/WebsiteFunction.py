from shared_functions import DataProcessing
from respective_websites.vpngate.vpngate_filter import VpnFilter
from respective_websites.vpngate.vpngate_connection import VpnSelection, Connection

class Vpngate:
	def update(File_Path):
		DataProcessing.appendNewList(File_Path)
	def filter(Folder_Path, File_Name):
		VpnFilter.ChooseFilterWay.filter(Folder_Path, File_Name)
	def connection(Source, Filtered_Csv_Path):
		vpn_hostname, vpn_ip, vpn_country = VpnSelection.selectOne(Source, Show_List = "y")
		ovpn_file_content = VpnSelection.decodeSelectedVpn(Filtered_Csv_Path, vpn_hostname)
		Connection.systemIdentify(vpn_hostname, vpn_ip, vpn_country, ovpn_file_content)
