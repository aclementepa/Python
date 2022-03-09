import webbrowser
import os
import time
import requests
import subprocess


def DownloadPrograms():
    # download & save installer
    installer_location = "H:\\Setup\\TightVNC\\"
    vnc_url = "https://www.tightvnc.com/download/2.8.63/tightvnc-2.8.63-gpl-setup-64bit.msi"
    r = requests.get(vnc_url, allow_redirects=True)
    open((installer_location + 'tightvnc.msi'), 'wb').write(r.content)

    
def InstallPrograms():    
    os.system("msiexec /i H:\\Setup\\tightvnc.msi /quiet /norestart /log H:\\Logs\\TightVNC-install.log ADDLOCAL='Server' VIEWER_ASSOCIATE_VNC_EXTENSION=1 SERVER_REGISTER_AS_SERVICE=1 SERVER_ADD_FIREWALL_EXCEPTION=1 VIEWER_ADD_FIREWALL_EXCEPTION=1 SERVER_ALLOW_SAS=1 SET_USEVNCAUTHENTICATION=1 VALUE_OF_USEVNCAUTHENTICATION=1 SET_PASSWORD=1 VALUE_OF_PASSWORD=h!si9ns SET_USECONTROLAUTHENTICATION=1 VALUE_OF_USECONTROLAUTHENTICATION=1 SET_CONTROLPASSWORD=1 VALUE_OF_CONTROLPASSWORD=h!si9ns")
    os.system("msiexec /i H:\\Setup\\MitelConnect.exe /q /norestart /log H:\\Logs\\Mitel-install.log")


# download 

DownloadPrograms()
InstallPrograms()

# download vnc
# os.system('msiexec /i %s /qn' % msi_location)

# start programs



# os.startfile("\\\\telperion\\installers")
# os.startfile("C:\\Program Files\\PremiumSoft\\Navicat for MySQL\\navicat.exe")
# os.startfile("C:\\Program Files (x86)\\Mitel\\Connect\\Mitel.exe")
# os.startfile("C:\\Users\\anthony.clemente\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
# os.startfile("C:\\Users\\anthony.clemente\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
# os.startfile("C:\\Users\\anthony.clemente\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Howard Industries\\Timeclock\\Timeclock.appref-ms")

os.startfile("C:\\Users\\anthony.clemente\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")