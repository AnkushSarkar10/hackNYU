import requests
from datetime import datetime
import json


# fictional calender - https://calendar.google.com/calendar/u/0/embed?src=atlasobscura.com_3un9ajpqcp8gapehkt4ahlu6io@group.calendar.google.com&ctz=America/New_York

api_key = "AIzaSyAUJTOFWluCTgRzQY5LgSDkbMMsjDaPo-I"
countrycode = "canadian"
countrycode_list = ["canadian", "indian", "usa", "uk"]
url = f"https://www.googleapis.com/calendar/v3/calendars/en.{countrycode}%23holiday%40group.v.calendar.google.com/events?key={api_key}"

r = requests.get(url)
data_json = r.json()


for i in data_json["items"]:
    curr_date = i["start"]["date"]
    curr_date_obj = datetime.strptime(curr_date,"%Y-%m-%d")
    curr_holiday = i["summary"]
    if curr_date_obj.year == 2022:
        print(curr_date_obj,curr_holiday)