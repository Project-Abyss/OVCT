# OVCT (Public VPN Connection Tool)
***OVCT***  is a tool built with Python web crawling technique.

After collecting the public VPN list conforming to the OpenVPN protocol from the vpngate website, it allows user to select specific VPN ISP hostname and drive the OpenVPN software to assist in connection.

This repository contains:
1. A connection tool of Public VPN
2. A document of codeing rules

## Install
### Requirements
* Python 3.x
* Software `OpenVPN` 
* Python package `pandas`

### Software: `OpenVPN`
* Linux
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
* Linux
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

## Usage
* Initialize VPN list
  ```
  $ python3 initialize.py
  ```
* Main Function ( Update & Filter & Connect )
  ```
  $ python3 ovct.py
  ```

## Contributing
[黃丰嘉 Feng-Chia Huang](https://github.com/bessyhuang)@Abyss-TeamA (Project Manager/Maintainer)<br />
[許至齊 Zhi-Qi Xu](https://github.com/xkeBANg)@Abyss-TeamA (Author/Maintainer)<br />
[黃子軒 Tzu-Hsuan Huang](https://github.com/Nima-Huang)@Abyss-TeamA (Author/Maintainer)<br />
[宋安琪 An-Chi Sung](https://github.com/Anzheim)@Abyss-TeamB (Project Manager/Maintainer)<br />
[許雅喬 Ya-Chiao Hsu](https://github.com/Chiao52)@Abyss-TeamB (Author/Maintainer)<br />
[王筱鈞 Hsiao-Chun Wang](https://github.com/momo8042)@Abyss-TeamB (Author/Maintainer)
