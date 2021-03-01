import requests

res = requests.get('http://127.0.0.1:5000/users/8')

print(res.json())

