import requests, pyperclip

url = ""
while True:
    contenido_actual = pyperclip.paste()
    if contenido_actual != url:
        content = requests.get(contenido_actual)
        content.raise_for_status()
        html = open('Web.html', 'wb')
        for chunk in content.iter_content(100000):        
            html.write(chunk)
        url = contenido_actual
        print(contenido_actual)
            

                

