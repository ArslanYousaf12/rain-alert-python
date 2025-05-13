import requests

API_KEY = YOU_API_KEY
LAT = "30.969349"
LONG = "70.942795"
OWP_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

para = {
    "lat":LAT,
    "lon":LONG,
    "appid":API_KEY
}
res = requests.get(url=OWP_ENDPOINT, params=para)
res.raise_for_status()
data = res.json()
print(data)


