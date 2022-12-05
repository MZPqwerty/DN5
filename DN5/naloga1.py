import requests

def get_html(url):
    zahteva = requests.get(url)
    koda = zahteva.status_code

    if koda == 200:
        return zahteva.text

    else:
        return False

page1 = get_html('https://example.com/')
page2 = get_html('http://example.com/neobstaja')

print(page1)
print(page2)