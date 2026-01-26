import json
import requests


api_key = "cd75f5ca4453021a800d8fa01e910407"

query = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric"

try:
    res = requests.get(url)
    if res.status_code == 200:
        res_json = res.json()
        # print(json.dumps(res_json, indent=2))

        print(f"Weather: {res_json["weather"][0]["description"]}")
        print(f"Temperature: {res_json["main"]["temp"]} Celsius")
except requests.exceptions.RequestException as e:
    print ("Error during request:", e)
