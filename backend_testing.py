import requests
import db_connector

try:
    res = requests.post('http://127.0.0.1:5000/users/8', json={"user_name": "Alex"})
    check_user = requests.get('http://127.0.0.1:5000/users/8')

    #Setp 3 - print DB
    db_connector.get_all_info()

    print(res.json())
    print(check_user.json())
except:
    print("test failed")
