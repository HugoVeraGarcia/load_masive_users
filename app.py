from flask import Flask
import pandas as pd
import requests


app = Flask(__name__)

@app.route('/add_massive_users')
def add_massive_users():
    url = 'https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/export?format=csv&id=1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU&gid=135007174'
    df = pd.read_csv(url)
    for i in range(len(df)):
        first_name = df.iloc[i]['first_name']
        last_name = df.iloc[i]['last_name']
        email = first_name[0:3]
        email = email.lower()
        email = f"{email}{i}@gmail.com "
        password = i

        payload = {
        "name": first_name,
        "email": email,
        "password": password
        }

        # endpoint de ms users, debe estar levantado
        API_ENDPOINT = 'http://127.0.0.1:8000/v1/register'
        response = requests.post(url = API_ENDPOINT, data=payload)
    return {'status':'users added successfully'}
        

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)

