#!/usr/bin/env python3

import smtplib
import datetime as dt
import random

'''

Email a quote to the specified recipient on a specific day of the week.
"Return the day of the week as an integer, where Monday is 0 and Sunday is 6."
 - DAY_OF_WEEK variable reference above.
smtp.gmail.com was the mailing server of choice in this example. Acknowledge that this may very well change based on your own needs.

'''

MY_EMAIL = "your email"
MY_PASSWORD = "your password"
RECIPIENT = "send to this email"
DAY_OF_WEEK = 2


now = dt.datetime.now()
weekday = now.weekday()
if weekday == DAY_OF_WEEK:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT,
                msg=f"Subject: Hey there!\n\n{quote}"
            )
