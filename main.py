import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

sender_mail = "qalamochirgich@gmail.com"
password = "enpdjqayzsxcxqfv"

def send_email_def(receiver_mail):
    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = receiver_mail
    message['Subject'] = 'Using Threading'
    text = f'Assalomu alaykum, hurmatli {receiver_mail} egasi!'
    message.attach(MIMEText(text, 'plain'))
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(sender_mail, password)
            connection.sendmail(sender_mail,receiver_mail, message.as_string())
        print('Successfully sent! ')
    except Exception as e:
        print(f'Mission failed: {e}')


users = [
    'xosaxamid@gmail.com',
    'rakhmonovnazarboy0@gmail.com',
    'raxmonovnazarboy@gmail.com',
    'raxmonovnazarboy0@gmail.com',
    'rakhmonovnazarboy0@gmail.com',
    'killiyaezzov@gmail.com',
    'raxmonovnazarboy@gmail.com',
    'kimpsix@gmail.com',
    'azizolimov@gmail.com',
    'asilbekomonov@gmail.com',
    'asalortikova1256@gmail.com'
]

def send_email_one_by_one():
    for user in users:
        send_email_def(user)
    print('All emails are sent!')


thread1 = threading.Thread(target = send_email_one_by_one)
thread1.start()


full_name = input('Enter your full name: ')
print(full_name)