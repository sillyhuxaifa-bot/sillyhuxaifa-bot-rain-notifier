from datetime import datetime
import pandas
import random  
import smtplib
import os
 
 
 
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


def get_letter(name):    
     
    file_path = f"./letter_templates/letter_{random.randint(1 ,3)}.txt"

    with open(file_path) as tl:
        letter = tl.read()
        letter = letter.replace("[NAME]", name)
        return letter

         
def sendmail(name, email): 
          
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject: Happy Birthday!\n\n{get_letter(name)}")
                
                
today = datetime.now()
today_tuple = (today.month, today.day)   

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]
    sendmail(name, email)