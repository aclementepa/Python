from os import error
import subprocess
from datetime import date, datetime
import socket
import sys, getopt
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def InstallUpdates(address):

    host = address
    port = 22
    username = "python.scanner"
    password = "H0w@rd*S0l0"
    command = "powershell Get-WindowsUpdate -install -acceptall -IgnoreReboot"

    # powershell install-module PsWindowsUpdate -AcceptLicense -AllowClobber -Force
    # powershell Set-ExecutionPolicy -Scope LocalMachine Bypass
    # powershell import-module PSWindowsUpdate
    # powershell Enable-PSRemoting
    # powershell Set-Item wsman:\localhost\client\trustedhosts HOWARD-48 -orce
    # powershell Restart-Service WinRM
    # powershell Set-ExecutionPolicy -Scope LocalMachine Restricted

    login_credentials = "anthony.clemente@" + host
    p = subprocess.Popen(["cmd.exe", "ssh anthony.clemente@"])
    p = subprocess.Popen(["powershell.exe", "Get-WindowsUpdate -install -acceptall -IgnoreReboot"], stdout=sys.stdout)
    p.communicate()
def RemoteCommands(address):
    
    import paramiko
    try:
        port = 22
        username = "python.scanner"
        password = "H0w@rd*S0l0"
        policy_update = "gpupdate /force"
        sfc_scan = "sfc /scannow"
        output = []

        print("Starting Remote Connection")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address, port, username, password)
        stdin, stdout, stderror = ssh.exec_command(policy_update)
        policy_output = stdout.readlines()
        stdin, stdout, stderror = ssh.exec_command(sfc_scan)
        sfc_output = stdout.readlines()
        ssh.close()
        print(policy_output)
        print(sfc_output)
        print("Remote Connection Closed")

        output.append(address + ": \n Group Policy Results: " + policy_output + "\n SFC Output: " + sfc_output + "\n\n")
    except(error):
        output.append(address + ": Error " + error + "\n")
    return output
    # login_credentials = username + host
    # p = subprocess.Popen(["cmd.exe", "ssh anthony.clemente@"])
    # p = subprocess.Popen(["powershell.exe", "Get-WindowsUpdate -install -acceptall -IgnoreReboot"], stdout=sys.stdout)
    # p.communicate()
def ScanNetwork():
    results = ["Results for Network Scan"]
    addresses = []
    # totalPings = 255-50
    for ping in range(51,255):
        # percentComplete = str(round(ping / totalPings)) + "%"
        # print(percentComplete)
        address = "192.168.100." + str(ping)
        res = subprocess.call(['ping', address])
        # res = subprocess.call(['ping', address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)        Quiet Mode
        try:
            host = socket.gethostbyaddr(address)
            temp = str(host[0]) + " (" + str(host[2]) + ")"
            if ("HOWARD") in temp:
                if("CLOVIS" or "DESKTOP" or "ITHIL" or "ZEFFO" or "EPSON" or "HP" or "ISIGNS"or "BROTHER" or None) in temp:
                    addresses.append(address)
            else:
                # remove unwanted devices
                subprocess.call(BuildRemoveDNSCommand(address, host[0]))
                subprocess.call(BuildRemoveDHCPCommand(address))
        except:
            temp = "Unidentified: " + address
        if res == 0:
            res = ""
        else:
            # RemoveDHCPResult = subprocess.call(BuildRemoveDHCPCommand(address))
            if res == 1:
                results.append("Failed ping to " + temp)
            if res == 2:
                results.append("No response from " + temp)
    return results

def WriteResultstoFile(results, filepath):
    f = open(filepath, "x")
    for result in results:
        f.write(result + "\n")
def SendEmail(sender, receiver, body, subject, filepath):
        
    smtp_server = "mail.howardindustries.com"
    port = 587  # For starttls

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with open(filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        
    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header("Content-Disposition", f"attachment; filename= NetworkScanResults-" + str(date.today()) + ".txt",)

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()


    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.howardindustries.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)

def BuildRemoveDHCPCommand(ipAddress):
    return("powershell.exe Remove-DhcpServerv4Lease -ComputerName 'telperion.howardindustries.local' -IPAddress " + ipAddress)

def BuildRemoveDNSCommand(hostName, ipAddress):
    return("powershell.exe Remove-DnsServerResourceRecord -ComputerName 'telperion.howardindustries.local' -ZoneName 'howardindustries.local' -Name '" + hostName + "' -RRType 'A' -RecordData '" + ipAddress  + "'")

def RemoveRecords(ipAddresses, hostName):
    for ip in ipAddresses:
        print("Removed: " + 1)
        print("Removed: " + 1)

sender = ""
password = ""

try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["username=","password="])
except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-u", "--username"):
        sender = arg
    elif opt in ("-p", "--password"):
        password = arg

print("Beginning processes at " + str(datetime.now()))
scanResults = ScanNetwork()
print(scanResults)
filepath = "C:\\Development\\Reports\\NetworkScan\\NetworkScanResults-" + str(date.today()) + ".txt"
WriteResultstoFile(scanResults, filepath)
subject = " Network Scan Results - " + str(date.today())
body = "Results from the Network Scan of " + str(date.today()) +"\n\n"
for res in scanResults:
    body += "\n" + res
receiver_email = "anthonyc@howardindustries.com"
# body += "\nThese IP Addresses have been deleted from the domain."
SendEmail(sender, receiver_email, body, subject, filepath)