# Public-VPN-Connection-Tool

#### GitHub

https://github.com/Abyss-TeamA/Public-VPN-Connection-Tool

#### Author / Maintainers

[黃丰嘉 Feng-Chia Huang](https://github.com/bessyhuang)@[Abyss-TeamA](https://github.com/Abyss-TeamA) (Project Manager/Maintainer)<br />
[許至齊 Zhi-Qi Xu](https://github.com/xkeBANg)@[Abyss-TeamA](https://github.com/Abyss-TeamA) (Author/Maintainer)<br />
[黃子軒 Tzu-Hsuan Huang](https://github.com/Nima-Huang)@[Abyss-TeamA](https://github.com/Abyss-TeamA) (Author/Maintainer)<br />

---
## Introduction（專案概述）
製作一個使用 Python 撰寫的「 Public VPN Connection Tool 」。

透過 Python 爬蟲方法，從 VPN Gate 網站 爬取符合 OpenVPN protocol 的 public VPN 清單後，提供甲方選擇並驅動 OpenVPN 軟體協助掛載。


---
## Features
* Support Ubuntu Linux, Windows, MacOS
* Provide 3 advanced filtering functions
* Automatically crawl public VPN list and connect to public VPN.

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
    * Define the decoder and save as ovpn file (Converts Base64 to ASCII)
* `connection.py`
    * Connect to public vpn by using OpenVPN software
    * It supports 3 operating systems: Ubuntu, Windows, MacOS

---
## Installation（如何安裝）

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
## Usage（如何使用）

### Ubuntu Linux

### Windows


### MacOS

---
## Resources
* [Connecting to Access Server with Linux](https://openvpn.net/vpn-server-resources/connecting-to-access-server-with-linux/)
* [Command Line Functionality for OpenVPN Connect](https://openvpn.net/vpn-server-resources/command-line-functionality-for-openvpn-connect/)
* [VPN Gate - Public Free VPN Cloud by Univ of Tsukuba, Japan](https://www.vpngate.net/en/)
