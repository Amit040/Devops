import psutil
import smtplib
from email.mime.text import MIMEText

#check memory usage
def check_memory_consumption():
    current_usage=psutil.virtual_memory()
    return current_usage.percent

def send_email(subject,body):
    sender_email="gcpexampre@gmail.com"
    receiver_email="amit.ec94@gmail.com"
    Password="iqqo qbxh steb sqhl"

    msg=MIMEText(body)
    msg['TO']=receiver_email
    msg['FROM']=sender_email
    msg['subject']=subject

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls() #For Encription
        server.login(sender_email, Password)
        server.send_message(msg)
    
def main():
    Current_Usage=check_memory_consumption()
    if Current_Usage >=50:
        send_email("Warning:Memory Usage is high",f"Current usage:{Current_Usage}")
        print("Task completed")
    else:
        print("Memory Usage is normal")
#To Automatute the process, calling main function
main()

