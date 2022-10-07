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
    password = "password"
    command = "powershell Get-WindowsUpdate -install -acceptall -IgnoreReboot"


    login_credentials = "test.user@" + host
    p = subprocess.Popen(["cmd.exe", "ssh test.user@"])
    p = subprocess.Popen(["powershell.exe", "Get-WindowsUpdate -install -acceptall -IgnoreReboot"], stdout=sys.stdout)
    p.communicate()
def RemoteCommands(address):
    
    import paramiko
    try:
        port = 22
        username = "python.scanner"
        password = "password"
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
def ScanNetwork():
    results = ["Results for Network Scan"]
    addresses = []
    for ping in range(51,255):
        address = "192.168.100." + str(ping)
        res = subprocess.call(['ping', address])
        try:
            host = socket.gethostbyaddr(address)
            temp = str(host[0]) + " (" + str(host[2]) + ")"
            if ("COMP") in temp:
                if("SERVER" or "DESKTOP" or None) in temp:
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
        
    smtp_server = "mail.server.com"
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
    with smtplib.SMTP_SSL("mail.server.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)

def BuildRemoveDHCPCommand(ipAddress):
    return("powershell.exe Remove-DhcpServerv4Lease -ComputerName 'computer.domain.local' -IPAddress " + ipAddress)

def BuildRemoveDNSCommand(hostName, ipAddress):
    return("powershell.exe Remove-DnsServerResourceRecord -ComputerName 'computer.domain.local' -ZoneName 'domain.local' -Name '" + hostName + "' -RRType 'A' -RecordData '" + ipAddress  + "'")

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
receiver_email = "anthonyc@server.com"
# body += "\nThese IP Addresses have been deleted from the domain."
SendEmail(sender, receiver_email, body, subject, filepath)