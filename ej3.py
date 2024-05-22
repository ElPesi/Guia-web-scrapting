import requests
import pyperclip
from bs4 import BeautifulSoup
import os

def obtenerPagina(url):
    pag = requests.get(url)
    pag.raise_for_status()
    if pag.status_code == 200:
        soup = BeautifulSoup(pag.text, 'html.parser')
        a = soup.find_all('article')
        return a
    
url = pyperclip.paste()
print("hola")
while True:
    if pyperclip.paste() != url:
        url = pyperclip.paste()
        web = requests.get(url)
        web.raise_for_status()
        soup = BeautifulSoup(web.text, 'html.parser')
        divsLinks = soup.find_all('div')
        for div in divsLinks:
            for link in div.find_all('a'):
                print(link.get('href'))
