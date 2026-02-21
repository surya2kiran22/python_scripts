import requests
import json

def weather(city):
    api_key = '86535768e4c5b535730eb70bff1a8501'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    param = {'q':city,'appid':api_key,'units':'metric'}
    res = requests.get(base_url,params=param)
    if res.status_code == 200:
        print("valid response with status code 200")
    else:
        print("invalid response enter valid city")
        exit()
    data = res.json()
    #print(json.dumps(data,indent=3))
    des = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    #print(res.url)
    return f"The temperature is {temp} and humidity is {humidity} with {des}"


city = input("enter city name: ")
print(weather(city))