import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


api_key_currency = os.getenv('api_key_currency')
def curency_code():
    codes =[]
    url_curr_code = f'https://v6.exchangerate-api.com/v6/{api_key_currency}/latest/USD'
    res = requests.get(url_curr_code)
    print(res.status_code)
    if res.status_code != 200:
        print("invalid response ")
        exit()
    data = res.json()
    conv_codes = data["conversion_rates"]
    codes=list(conv_codes.keys())
    return codes


def conversion_rate(base,target,amount = 1.0):
    base = base.upper()
    target = target.upper()
    amount = float(amount)
    print(amount)
    url = f'https://v6.exchangerate-api.com/v6/{api_key_currency}/pair/{base}/{target}/{amount}'
    res = requests.get(url)
    print(res.status_code)
    if res.status_code != 200:
        print("invalid response enter valid currency")
        exit()
    data = res.json()
    conv_rate = data["conversion_rate"]
    conv_res = data["conversion_result"]
    #print(conv_rate)
    return f"The conversion for {base} to {target} is {conv_rate} and conversion amount is {conv_res}"

def main():
    try:
        print("list of currency codes ",curency_code())
        b = input("eneter base currency like USD, INR,EUR: ")
        t = input("eneter target currency like USD, INR,EUR: ")
        amt = int(input("enter amount : "))
        print(conversion_rate(b,t,amt))
    except:
        print("enter valid input ")

main()

