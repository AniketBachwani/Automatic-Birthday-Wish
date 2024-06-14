import smtplib
import datetime as dt
import random

f = open('quotes.txt')
lines = f.readlines()

i = random.randint(1, 102)
quote = lines[i]

mail_id = "abachwani77@gmail.com"
password = "wsxmmncmkerqqhim"

now = dt.datetime.now()
day = now.weekday()
print(day)
if day == "1":

    with smtplib.SMTP("smtp.gmail.com") as use_it:
        use_it.starttls()
        use_it.login(user=mail_id, password=password)
        use_it.sendmail(from_addr=mail_id,
                        to_addrs="aniketbachwani0@gmail.com",
                        msg=f"subject:Happy Birthday\n\nf{quote}")
