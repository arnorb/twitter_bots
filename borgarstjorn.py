# encoding: utf-8

'''
  borgarstjorn.py
    A simple twitter bot
'''

from datetime import datetime
import calendar
import tweepy

today = datetime.today().date()
current_month = today.month
current_year = today.year
first_tuesday = calendar.Calendar(1).monthdatescalendar(current_year,current_month)[1][0]
third_tuesday = calendar.Calendar(1).monthdatescalendar(current_year,current_month)[3][0]
fundir = [first_tuesday, third_tuesday, today]

CONSUMER_KEY = 'qs05jklgCleQ3c7hIA2OvbOV4'
CONSUMER_SECRET = 'QqgnOBK2FlhSd0eDsWGkdi7OF90O3Mu6wIYNHcVmWytqyBGeFm'
ACCESS_TOKEN = '3137303357-0YCjcqiVZuKm6w1OBxNo7wKohEJ4KO9j5gUjHTe'
ACCESS_SECRET = '6rFOxwRGAsOr3mCVBz2KrdgQns4caIpmezIpqc7lVq7RY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

message = 'Borgarstjórnarfundur hefst kl. 14:00'

if today in fundir:
    api.update_status(status=message)
