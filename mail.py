import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

# module for storing password
import passwords

# { provide all this 
fromaddr = "1anujgupta123@gmail.com"
toaddr = "1anujgupta123@gmail.com"
filename = "user.jpg"       # this file will be sent
gmail_password = passwords.gmail
# }

def mail_function():
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "USER DETECTED"
        body = "THESE IS USER NO() ----- "
        msg.attach(MIMEText(body, 'plain'))

        attachment = open("user.jpg", "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',
                     "attachment; filename= %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # stored file secretly on my device need to put ur pass their
        s.login(fromaddr, gmail_password)   #put either ur pass directly here or make a seperate file and import here 
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)

        s.quit()
        time.sleep(1)

        print("Mail send")
        
mail_function()
#---------------------------------------------------