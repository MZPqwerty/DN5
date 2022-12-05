import requests
import json

def get_api_data(url):
    zahteva = requests.get(url)
    koda = zahteva.status_code

    if koda == 200:
        dictionary = json.loads(zahteva.text)
        return dictionary

    else:
        return False

data1 = get_api_data('https://jsonplaceholder.typicode.com/todos/1')
data2 = get_api_data('https://jsonplaceholder.typicode.com/nedala/nedala')

print(data1)
print(data2)