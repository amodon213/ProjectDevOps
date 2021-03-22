import requests
from db_connector import *
try:
    res = requests.post('http://127.0.0.1:5000/users/8', json={"user_name": "Alex"})  # Adding Alex with User ID 8
    check_user = requests.get('http://127.0.0.1:5000/users/8')  # Step 2 - Checking user ID - 2

except:
    print("FAILED TO FETCH INFORMATION")
finally:
    print(res.json())
    print(check_user.json())
    get_all_info()  # Step 3 - Printing the entire table



