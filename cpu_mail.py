import psutil
import time
import smtplib
from email.mime.text import MIMEText
while True:
    time.sleep(1)
    if psutil.cpu_percent() < 100:
        mail_host = 'smtp.server'
        mail_user = 'sender_name'
        mail_pass = 'password'
        sender = 'sender_mail'
        receivers = ['receiver_mail']
        message = MIMEText('content', 'plain', 'utf-8')
        message['Subject'] = 'title'
        message['From'] = sender
        message['To'] = receivers[0]
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            smtpObj.quit()
            print('success')
            break
        except smtplib.SMTPException as e:
            print('error', e)
            break
