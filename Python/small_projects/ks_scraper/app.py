import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests
import time


def send_notif(url, title):
    sender_email = "cesarmailserver@gmail.com"
    receiver_email = "cqann.lindberg@gmail.com"
    file = open("pass.txt")
    password = file.readline()#input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
    <body>
        <p>Hejsan!<br>
        En ny annons med dina söktermer har lagts upp på klocksnack!<br>
        <a href="{}">{}</a> <br>
        Hoppas det hjälper!
        </p>
    </body>
    </html>
    """.format(url,title)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )



url = "https://klocksnack.se/search/12204727/?q=oyster+perpetual&o=date&c[node]=11"
last = ""
not_first = True

while True:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    latest_post = soup.findAll("li")[0]

    if last != latest_post and not_first:
        h3 = latest_post.find("h3")
        h3_title = h3.find("a")
        title = h3_title.text
        dir_url = "https://klocksnack.se/" + h3_title["href"]
        send_notif(dir_url, title)

    not_first = True
    last = latest_post
    break
    time.sleep(5 * 60)
