import pandas as pd
import requests

def coon_pool_to_google_spreadsheet(sheet_id):
    return f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&id={sheet_id}&gid=135007174'

sheet_id = '1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU'
url = coon_pool_to_google_spreadsheet(sheet_id=sheet_id)
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

    API_ENDPOINT = 'http://127.0.0.1:8000/v1/register'
    response = requests.post(url = API_ENDPOINT, data=payload)
    
    
    response = response.json()

