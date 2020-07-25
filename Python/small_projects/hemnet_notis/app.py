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
    message["Subject"] = "Ny Hemnet Annons!"
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
        En ny annons med dina söktermer har lagts upp på Hemnet!<br>
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



url = "https://www.hemnet.se/bostader?location_ids%5B%5D=924030&location_ids%5B%5D=473991&item_types%5B%5D=bostadsratt&rooms_min=1&price_max=3000000"
last = ""
not_first = True

while True:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    ad_list = soup.findAll("ul")[11]
    house_ads = [x for x in ad_list.findAll("li") if x["class"] == ['normal-results__hit', 'js-normal-list-item']]
    latest_house = house_ads[0]
    house_link = latest_house.find("a")["href"]
    info_dic = eval(latest_house["data-gtm-item-info"].replace("true","True"))
    house_name = info_dic["name"]
    
    if last != house_link and not_first:
        send_notif(house_link, house_name)

    not_first = True
    last = house_link
    time.sleep(5 * 60)
