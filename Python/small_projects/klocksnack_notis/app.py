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
    message["Subject"] = "Ny Klocksnack Annons!"
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



url = "https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/"
last = ""
first  = True
saved = set()
budget = 2000

while True:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    ad_list = None
    for i in soup.findAll("div"): 
        if i["class"] == ["structItemContainer-group", "js-threadList"]:
            ad_list = i
            break
    for ad in ad_list.findAll("div"):
        if ad["class"] != ["structItem-title"]: continue
        tag = ad.findAll("a")[0]
        if tag["class"] != ["labelLink"]: continue
        
        tag_span = tag.find("span")
        print(tag_span.contents[0])
        title = ad.findAll("a")[1]
        ad_name = title.contents[0]
        if ad_name not in saved:
            saved.add(ad_name)
            href = title["href"]
            link = "https://klocksnack.se" + href
            ad_page = requests.get(link)
            ad_soup = BeautifulSoup(ad_page.content, "html.parser")
            price = ad_soup.findAll("dd")[0].contents[0]
            failed = False
            int_price = None
            try:
                int_price = int(price.strip())
            except:
                print("fail")
                failed = True
            if not failed and int_price < budget and not first:
                print("emailed")
                #send_notif(link, ad_name)
                time.sleep(3)
        

    first = False
    time.sleep(5 * 60)
