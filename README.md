# OVCT (Public VPN Connection Tool)

#### GitHub

https://github.com/Project-Abyss/OVCT

#### Author / Maintainers

[黃丰嘉 Feng-Chia Huang](https://github.com/bessyhuang)@[Abyss-TeamA](https://github.com/Abyss-TeamA) (Project Manager/Maintainer)<br />
[許至齊 Zhi-Qi Xu](https://github.com/xkeBANg)@[Abyss-TeamA](https://github.com/Abyss-TeamA) (Author/Maintainer)<br />
[黃子軒 Tzu-Hsuan Huang](https://github.com/Nima-Huang)@[Abyss-TeamA](https://github.com/Abyss-TeamA) (Author/Maintainer)<br />

---
## Introduction
***OVCT*** is a tool built with Python web crawling technique.

After collecting the public VPN list conforming to the OpenVPN protocol from the vpngate website, it allows user to select specific VPN ISP hostname and drive the OpenVPN software to assist in connection.

---
## Features
* Support Ubuntu Linux, Windows, MacOS
* Provide 3 advanced filtering functions
* Automatically crawl public VPN list and connect to public VPN.

---
## System Structure
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/42068007/203088995-583d5b55-5b0c-49c7-ae34-c4ebbc28f763.png">

---
## Explanation
* `main.py`
    * The main program
* `webcrawler.py`
    * Define the web crawler and update the public vpn list
    * There is 1 resource (website): vpngate
* `vpnfilter.py`
    * Define the vpn filter and save as csv file
    * There are 3 filter criteria: Country, Speed, Without filtering
* `vpnselection.py`
    * Define the vpn selection
* `decode.py`
    * Define the decoder and convert the ovpn file content from Base64 to ASCII
* `connection.py`
    * Connect to public vpn by using OpenVPN software
    * It supports 3 operating systems: Ubuntu, Windows, MacOS

---
## Installation

### Requirements
* Python 3.x
* Software `OpenVPN` 
* Python package `pandas`

### Software: `OpenVPN`
* Ubuntu Linux
   * Step1: Open `Terminal`
   * Step2: Input command: 
      ```
      $ sudo apt install openvpn
      ```
* Windows
   * Step1: Download [OpenVPN GUI](https://openvpn.net/community-downloads/)
       * Note: Please follow your CPU (32bit / 64bit / ARM) choose a correct version.
   * Step2: Double click to install `OpenVPN GUI` software
* MacOS
   * Step1: Download [OpenVPN Connect for macOS](https://openvpn.net/downloads/openvpn-connect-v3-macos.dmg)
   * Step2: Double click to install `OpenVPN Connect` software

### Python Package: `pandas`
* Ubuntu Linux
   ```
   $ sudo apt install python3-pandas
   ```
* Windows
   ``` 
   $ pip install pandas
   ```
* MacOS
   ```
   $ pip3 install pandas
   ```

---
## Usage
```
$ python3 main.py
```

### Ubuntu Linux
* Select the function to update VPN lists, filter lists, or connections.  
   * Update public VPN list:  
      * Save new public VPN list.   
   * Filter the list:  
      * Choose a mode to filtering list and save it.  
   * Connection:  
      * Enter the OpenVPN software path (Default: `/etc/openvpn`) and ovpn file will save to `/etc/openvpn/client`.    
      * Select a list and enter the hostname,  you will get an ovpn file & connect.  

### Windows
* Select the function to update VPN lists, filter lists, or connections.  
   * Update public VPN list:  
      * Save new public VPN list.   
   * Filter the list:  
      * Choose a mode to filtering list and save it.  
   * Connection:  
      * Select a list and enter the hostname,  you will get an ovpn file . 
      * enter the OpenVPN software path (Default: `C:\Users\[user_name]\OpenVPN`) and ovpn file will save to `C:\Users\[user_name]\OpenVPN\config`.  
*  Open the OpenVPN GUI and select the VPN data to connecting.  

### MacOS

* Enter the OpenVPN software path. (Default: `/Applications/OpenVPN Connect/OpenVPN Connect.app/Contents/MacOS/OpenVPN Connect`)
* Enter the hostname to get the ovpn file.
* Open the OpenVPN Connect APP and select the VPN data to connecting.

* Select the function to update VPN lists, filter lists, or connections.  
   * Update public VPN list:  
      * Save new public VPN list.   
   * Filter the list:  
      * Choose a mode to filtering list and save it.  
   * Connection:  
      * Enter the OpenVPN software path Default: `/Applications/OpenVPN Connect/OpenVPN Connect.app/Contents/MacOS/OpenVPN Connect`).  
      * Select a list and enter the hostname,  you will get an ovpn file .  
*  Open the OpenVPN GUI and select the VPN data to connecting. 

---
## Resources
* [Connecting to Access Server with Linux](https://openvpn.net/vpn-server-resources/connecting-to-access-server-with-linux/)
* [Command Line Functionality for OpenVPN Connect](https://openvpn.net/vpn-server-resources/command-line-functionality-for-openvpn-connect/)
* [VPN Gate - Public Free VPN Cloud by Univ of Tsukuba, Japan](https://www.vpngate.net/en/)
