# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:05:02 2019

@author: loren
"""
import requests
import config

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/{}.mailgun.org/messages.format(config.messages)",
        auth=("api", config.api_key ),
        data={"from": "Loren Bristow <lorendup@gmail.com>",
              "to": "Loren Bristow <lorendup@gmail.com>",
              "subject": "Hello Loren Bristow",
              "text": "Congratulations crazy, you just sent an email with Mailgun!  You are truly awesome!"})
send_simple_message()
