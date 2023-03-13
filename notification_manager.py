# This class texts the user with information of each flight that is lower than historical low prices.
# Users who signed up using sign_up.py are sent emails with flight info and a link to book the flight

import os
from dotenv import load_dotenv
import smtplib

load_dotenv(".env.txt")
my_email = os.getenv("my_email")
email_password = os.getenv("email_password")

class NotificationManager:

    def send_emails(self, user_info, flight_link, full_text):
        for user in user_info:
            user_email = user["email"]

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=email_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=user_email,
                    msg=f"Subject: New Low Price Flight!\n\n{full_text}.\nLink:{flight_link}".encode('utf-8')
                )