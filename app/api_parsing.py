import requests
from datetime import datetime
import json

def get_holidays(day, month, country):
    result = []

    payload  = {
    "api_key": "e9c15099a5eb94fe889eaca1c70c6fae9eb5634a",
    "country" : country,
    "year" : 2022,
    "day" : day,
    "month" : month
    }

    url = "https://calendarific.com/api/v2/holidays" 
    try:  
        r = requests.get(url,params=payload,timeout=0.8)
        data = r.json()
    except:
        data = {
                "response":{
                    "holidays": []
                    }
                }

    for i in data["response"]["holidays"]:
        holiday_name = i["name"] 
        result.append(holiday_name)
    
    print("done " + country)
    return result

def get_holiday_data(day, month):
    d = {}
    country_codes = [["IN","India"], ["CA", "Canda"], ["UK","United Kingdom"], ["CN", "China"], ["DE", "Germany"], ["JP", "Japan"], ["KR", "Korea"], ["FR", "France"],["MX", "Mexico"], ["AU", "Australia"], ["BR", "Brazil"]]
    for i in country_codes:
        try:
            l = get_holidays(day, month, i[0])
            if len(l) > 0:
                d[i[1]] = l
        except:
            pass
    return d
