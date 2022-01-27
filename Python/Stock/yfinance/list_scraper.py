from bs4 import BeautifulSoup
import requests
from api import check_if_valid

def check_volume(suffix):
    url = "https://www.gurufocus.com" + suffix
    page = requests.get(url) 
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.findAll("div", {"class": "stock-summary-table fc-regular"})[0]
    str_value = table.findAll("div")[3]
    value = int(str_value.text.strip().replace(",",""))
    return value

file = open("codes.txt", "a")
for page in range(7,14):
    url = "https://www.gurufocus.com/stock_list.php?m_country[]=SWE&sort=price&order=desc&p=" + str(page) + "&n=100"
    page = requests.get(url) 
    soup = BeautifulSoup(page.content, 'html.parser')

    ajax = soup.find(id="ajax_content")
    table = ajax.find(id="R1")
    rows = [x for x in table.findAll() if x.name == "tr"]
    for stock in rows:
        code_link = stock.find("a")
        code = code_link.text
        if code[-6:] != "Sweden": continue
        new_code = code[:-6].replace(" ", "-") + "ST"

        value = stock.findAll("td")[2].text
        if value[:3] != "SEK": continue
        if not check_if_valid(new_code): continue
        print(code)
        file.write(new_code)
        file.write("\n")

file.close()
        
