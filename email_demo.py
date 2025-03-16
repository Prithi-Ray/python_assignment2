import smtplib
import random

def read_data_send_mail():
    
    try:
        f=open("st_mails.txt","r")
        st_mails=f.read()
        
        st_mails=st_mails.split(",")
        print(st_mails)
    except:
        print("file not availble")
        
    sender_email="prithiray0@gmail.com"

    for i in st_mails:
        otp_number=random.randint(0000,9999)
        print(otp_number)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, "giso uihp pbny iasd")
        message = f"Hi your OTP number is {otp_number}"
        s.sendmail(sender_email, i, message)
        print("mail sent successfully")
        s.quit()

        try:

            s.sendmail(sender_email, i, message)
            print("mail sent successfully")
            s.quit()
        except:

            print("mail not sent")

read_data_send_mail()