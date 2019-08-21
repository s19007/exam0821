import requests
from bs4 import BeautifulSoup

req = requests.get("https://gamewith.jp/kuronekowiz/")
bs = BeautifulSoup(req.text, 'html.parser')

file = open('text.text', 'w')

for i in bs.select("h3"):
    file.write(i.getText() + '\n')

file.close()
