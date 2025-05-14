import requests
from twilio.rest import Client


API_KEY = API_KEY
LAT = "4.710989"
LONG = "-74.072090"
OWP_ENDPOINT = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
account_sid = YOUR_ACCOUNT_ID
auth_token = YOUR_ACCESS_TOKEN
para = {
    "lat":LAT,
    "lon":LONG,
    "appid":API_KEY
}
res = requests.get(url=OWP_ENDPOINT, params=para)
res.raise_for_status()
data = res.json()
list_data = data["list"]
# print(list_data[0]["weather"])
bring_umbrela = False
for num in range(12):
    hourly_data = list_data[num]
    # print(hourly_data["weather"]["id"])
    if int(hourly_data["weather"][0]["id"]) < 700:
        print(hourly_data["weather"][0]["id"])
        bring_umbrela = True
        print(num)
if bring_umbrela:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid='MG5953858eb335c43e62b56a4b0c53ef0f',
    body='Its going to Rain today so bring your 🌂',
    to=YOUR_NUMBER
    )
    print(message.status)


    
else:
    print("you dont have to brings umbrela")


