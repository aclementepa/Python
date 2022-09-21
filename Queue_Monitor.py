# Program: Queue_Monitor.py
# Author: Anthony Clemente
# Last Modified: 9/7/2022
# Purpose: Dispose of stale print jobs clogging print queue for DMS Work Order Department Printing
#          A report with the results will be sent out by email at or after 5PM 
#          This task will run M-F


import os
from queue import Empty
import subprocess
import sys, getopt
import shutil
from datetime import date, datetime, timedelta, time
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Send_Email(sender, recipient, body, subject, filepath):
        
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
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
    part.add_header("Content-Disposition", f"attachment; filename= " + filepath,)

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.howardindustries.com", 465, context=context) as server:
        server.login(sender, "h!si9ns*dms")
        server.sendmail(sender, recipient, text)

def Check_Print_Queue(filepath):
    log = []
    try:
        queue_files = os.listdir(filepath)
        queue_files.sort
        subprocess.call("net stop spooler")
        for file in queue_files:
            try:
                # if file has not been printed within 45 minutes, delete it
                file = filepath + "\\" + file
                file_time = datetime.fromtimestamp(os.path.getmtime(file))
                comparisondatetime = file_time + timedelta(minutes=59)
                if(comparisondatetime <= datetime.now()):
                    log.append("File:  " + file + " has been in the queue since - (" + str(file_time) + ")\n")
            except OSError as error:
                log.append(error)
        subprocess.call("net start spooler")
    except OSError as error:
        log.append(error)
    return log

def Write_To_Log_File(logs, filepath):
    f = open(filepath, "a")
    f.writelines(logs)

def Read_Log_File(filepath):    
    f = open(filepath, "r")
    return f

filepath = "C:\\Print_Monitor_Logs\\Queue_Monitor-" + str(date.today()) + ".txt"
print_queue_filepath = "C:\Windows\System32\spool\PRINTERS"
# print_queue_filepath = "C:\Development\Tester"
logs = Check_Print_Queue(print_queue_filepath)
print(len(logs))
if len(logs) > 0:
    Write_To_Log_File(logs, filepath)

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

    logs = Read_Log_File(filepath)
    subject = "Print Queue Monitor Results - " + str(date.today())
    body = "Results from the Print Queue Monitor " + str(date.today()) +"\n\n"
    for log in logs:
        body += "\n" + log
    sender = "dms@howardindustries.com"
    recipient_email = "mis@howardindustries.com"
    Send_Email(sender, recipient_email, body, subject, filepath)