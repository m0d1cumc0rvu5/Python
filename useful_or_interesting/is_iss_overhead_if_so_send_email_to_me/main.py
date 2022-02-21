#!/usr/bin/env python3

'''

Email yourself when the ISS is in close proximity to your current LAT and LONG position.
Both the subject header and body of the email will contain text that informs you to, "look up!".
Ensure you input the proper LAT and LONG for a fully functional program.

'''

import requests, smtplib, time
from datetime import datetime

MY_EMAIL = "enter your email here"
MY_PASSWORD = "enter your password here"
#Enter your lat and long
MY_LAT = 
MY_LONG = 


def iss_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude)
    print(iss_longitude)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# run every 60 seconds and verify if parameters are True


while True:
    time.sleep(60)
    if iss_within_range() and night_time():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Look up!\n\nLook up!"
            )



