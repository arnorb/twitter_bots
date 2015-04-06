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
tuesday = calendar.Calendar(1).monthdatescalendar(current_year,current_month)
first_tuesday = tuesday[1][0]
third_tuesday = tuesday[3][0]
fundir = [first_tuesday, third_tuesday]

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

message = 'Borgarstjórnarfundur er nú að hefjast. Þú getur fylgst með í beinni. http://reykjavik.is/fundirborgarstjornar/borgarstjorn-i-beinni'

if today in fundir:
    api.update_status(status=message)
