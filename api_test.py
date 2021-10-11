import requests

response = requests.request('GET', url='http://127.0.0.1:5000/allegro/offers')
print(response.json())
