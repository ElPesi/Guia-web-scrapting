import pyperclip
import requests
import os
from bs4 import BeautifulSoup

url = pyperclip.paste()  
nameFile = 'PFDs'
pdf = []
while True:
    if pyperclip.paste() != url:
        print("hola    ")
        url = pyperclip.paste()
        web = requests.get(url)
        web.raise_for_status()
        html = BeautifulSoup(web.text, 'html.parser')
        p = html.find_all('p')

        for i in p:
            for j in i.find_all('a', href=True):
                href = j['href']
                if '.pdf' in href:
                    pdf.append(href)

        if pdf:
            os.makedirs(nameFile, exist_ok=True)
            for urlPdf in pdf:
                arch = requests.get(urlPdf)
                arch.raise_for_status()
                with open(os.path.join(nameFile, os.path.basename(urlPdf)), 'wb') as playFile:
                    for chunk in arch.iter_content(10000):
                        playFile.write(chunk)
