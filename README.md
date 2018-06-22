# SocialCopsChallenge
Solution to Problem - Amnesia towards application for back end intern at Social Cops.

### Amnesia
John has a certain kind of amnesia. Every hour, he forgets his name. He’s tired of setting an alarm on his very old phone which doesn’t allow setting cron alarm jobs.

He wants to hire you to create an application which will send him an SMS every hour to remind him of his name. He also wants you to make sure that he doesn’t get alarms during the night when he is asleep.

Since you don’t know which part of the world John lives in, you have to use an SMS provider which can send an SMS to nearly every country. Twilio is a nice service for sending out SMSes. However, sometimes Twilio’s SMS fails, in which case you have to send it again.

Please do the following:

1. Create a (basic) web based application where John can set his phone number
2. Send an SMS every one hour except at night
3. Try resending an SMS if it fails, but retry no more than 5 times. (There is only so much you can do!)
4. The web application should also log all the failed messages and tell John for how many hours the application has been running.

## Setup
1. Type `git clone https://github.com/ttanay/SocialCopsChallenge` in terminal and press Enter.
2. In file `challenge/credentials.py`, add your email_id in `GMAIL_ID` and password in `GMAIL_PASSWORD`.
3. Sign up on MSG91 and copy your auth-key and paste it in `MSG_URL` in the `challenge/credentials.py` file.
5. Change `DATABASES` settings variable in `challenge/settings.py` according to your need - AWS or sqlite3.
6. Enter command `python3 -m venv env` in terminal, press Enter.
7. Enter `source env/bin/activate` and press Enter.
8. Run the command `python3 manage.py makemigrations` in terminal.
9. Run the command `python3 manage.py migrate` in terminal.
8. Add the cronjobs to your crontab using command `python3 manage.py crontab add`. You may have to run `python3 manage.py crontab remove` first depending on the error message. [Reference: kraiz/django-crontab](https://github.com/kraiz/django-crontab)
9. Run the server using the command `python3 manage.py runserver`.
