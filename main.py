import os
import requests
import smtplib


ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "6ee22c93f474a75d237562bb10164367"


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
         
def send_mail(sub_msg):
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=sub_msg
        )   
         


                

parameters = {
    "lat": 24.9472,
    "lon": 66.9833,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["list"]


for x in data:
    weather_id = x["weather"][0]["id"]
    time = x["dt_txt"].split(" ")[1].split(":")[0]
    if weather_id < 900 and time == "18":
        print("It's gonna rain today!")
        send_mail("Subject:UMBRELLA\n\nIt's gonna rain today, bring an ☔")
