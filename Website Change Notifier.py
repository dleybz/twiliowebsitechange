#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#based on https://chrisalbon.com/python/web_scraping/monitor_a_website/
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup


# In[ ]:


my_phone = "" #The phone number you'd like to receive texts on
twilio_phone = "" #Your registered number on Twilio
url = "https://www.recreation.gov/camping/campgrounds/232449"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
today_soup = str(BeautifulSoup(response.text, "lxml"))
body = f"The website {url} has changed."


# In[ ]:


def send_text(ph1, ph2, body):
    client = Client()

    message = client.messages.create(
        to=ph1, 
        from_=ph2,
        body=body
    )


# In[ ]:


try:
    with open("last_soup", "r") as last_soup:
        if (today_soup != last_soup.read()):
            send_text(my_phone, twilio_phone, body)
            with open("last_soup", "w") as last_soup:
                last_soup.write(today_soup)
except FileNotFoundError:
    with open("last_soup", "w") as last_soup:
        last_soup.write(today_soup)

