import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests
import time


def send_notif():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "cesarmailserver@gmail.com"
    receiver_email = "cqann.lindberg@gmail.com"
    pass_file = open("pass.txt", "r")
    password = pass_file.readline()

    message = MIMEMultipart("yeye")
    message["Subject"] = "ALERT New Cases!"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
    <body>
        <p>Hi,<br>
        skriasdfasf?<br>
        <a href="http://www.realpython.com">Real Python</a> 
        has many great tutorials.
        </p>
    </body>
    </html>
    """

    text = MIMEText(html, "html")

    message.attach(text)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


url = "https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/aktuellt-epidemiologiskt-lage/"
last = ""
rel_h = ""
not_first = True

while True:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    headings = soup.findAll("h2")

    last = rel_h
    rel_h = headings[2]

    if last != rel_h and not_first:
        send_notif()

    not_first = True
    time.sleep(5 * 60)
