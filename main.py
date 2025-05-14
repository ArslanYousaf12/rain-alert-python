import requests

API_KEY = API_KEY
LAT = "4.710989"
LONG = "-74.072090"
OWP_ENDPOINT = "https://pro.openweathermap.org/data/2.5/forecast/hourly"

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
    print("You have to brings umbrela ")
else:
    print("you dont have to brings umbrela")


