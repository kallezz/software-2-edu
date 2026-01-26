import requests


url = "https://api.chucknorris.io/jokes/random"

try:
    res = requests.get(url)
    if res.status_code == 200:
        res_json = res.json()
        print(res_json["value"])
except requests.exceptions.RequestException as e:
    print ("Error during request:", e)
