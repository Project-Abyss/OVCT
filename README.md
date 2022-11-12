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
* Step1: Executive program.  
         ```
         $ python3 Public_VPN_Connection_Tool.py  
         ```  
* Step2: Search the resources based on the requirement of Public VPN.   
         ![image](https://user-images.githubusercontent.com/87530200/200848724-d047ee0e-cd5a-4151-9b34-b3ace512eaf4.png)          
* Step3: Input the path & file name where the PublicVPN list will save.  
         ![image](https://user-images.githubusercontent.com/87530200/200848978-0dd6f39a-f1a8-45c4-81ff-3a2a0e18723f.png)  
* Step4: Check out the export file and choose the VPN needed.  
         ![image](https://user-images.githubusercontent.com/87530200/200849465-46b83b27-bfc9-4a17-b0e0-38e38a91fd1f.png)  
* Step5: Enter the OpenVPN path where was downloaded.  
         ![image](https://user-images.githubusercontent.com/87530200/200849587-30fd5b7d-ee78-40a6-a6c6-1e5401a867e8.png)  
* Step6: Enter the Hostname of the VPN.  
         ![image](https://user-images.githubusercontent.com/87530200/200850731-56021a90-3654-40fb-b485-26c7c0921002.png)  
* Step7: Wating for the linking.  
         ![image](https://user-images.githubusercontent.com/87530200/200850880-4b943f7d-3a1d-49d1-bfc5-1250dd26d202.png)  
* Step8: successfully connected.  
         ![image](https://user-images.githubusercontent.com/87530200/200851181-adc84d87-9564-4c7e-9334-81f7cba43e0f.png) 
* Step9: Check IP address is connected.     
    ```
    $ ifconfig
    ```
    ![image](https://user-images.githubusercontent.com/87530200/200851348-222e34e5-616c-48a8-bdce-e8f128fe0f3e.png)
 
           

* Note: Please confirm whether the computer network condition is normal connection.

### Windows
* Step1: Executive program.  
         ```
         $ python Public_VPN_Connection_Tool.py  
         ```    
* Step2: Search the resources based on the requirement of Public VPN.   
          ![image](https://user-images.githubusercontent.com/87530200/200842407-3cacaba0-3ef7-4a9f-833e-35cdffd111a1.png)  
* Step3: Input the path where the PublicVPN list will save.   
         ![image](https://user-images.githubusercontent.com/87530200/200842683-4e489e6f-f172-4270-8e27-1e5f6f3a6e22.png)  
* Step4: Check out the export file and choose the VPN needed.   
         ![image](https://user-images.githubusercontent.com/87530200/200842983-6105d3b4-8811-4bbc-aeed-3326fdf22788.png)  
* Step5: Enter the OpenVPN path where was downloaded.   
         ![image](https://user-images.githubusercontent.com/87530200/200843302-a60a58c3-1527-43d0-bd09-f3a7583334cf.png)  
* Step6: Enter the Hostname of the VPN.   
         ![image](https://user-images.githubusercontent.com/87530200/200843673-3cb2dceb-1678-4511-ac32-61965a565cd9.png)  
* Step7: Right click the icon in the toolbar.   
         ![image](https://user-images.githubusercontent.com/87530200/200465979-ec64e26e-c71f-4838-9374-178afcc462a9.png)  
* Step8: Right click to connect when the VPN file is imported.   
         ![image](https://user-images.githubusercontent.com/87530200/200844937-2e23df06-601a-4f62-a5b2-d2a2143f1462.png)  
* Step9: Wating for the linking.   
         ![image](https://user-images.githubusercontent.com/87530200/200845039-a5efbd30-6f15-4978-b11c-f0d86f522e69.png)  
         ![image](https://user-images.githubusercontent.com/87530200/200845094-41327b99-8bcf-49e1-98b1-ca5688163c4d.png)  

### MacOS

---
## Resources
* [Connecting to Access Server with Linux](https://openvpn.net/vpn-server-resources/connecting-to-access-server-with-linux/)
* [Command Line Functionality for OpenVPN Connect](https://openvpn.net/vpn-server-resources/command-line-functionality-for-openvpn-connect/)
* [VPN Gate - Public Free VPN Cloud by Univ of Tsukuba, Japan](https://www.vpngate.net/en/)
