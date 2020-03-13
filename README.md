# WhatsApp ChatBot - COVID Bot

## How to Run Server

Simply git clone this repo.

> git clone <https://github.com/marcustut/WhatsApp_COVIDBot.git>

Install all required modules

> pip install twilio requests bs4 flask

To start the server run

> python covid-bot.py

To broadcast the server to the internet

> ngrok http 5000

simply copy the link given by ngrok and copy it to your Twilio Sandbox Configuration.

## Bot Usages

covid help - display help message.

covid all - show the worldwide COVID-19 status

covid _country_ - show the COVID-19 status for this country

> eg. _covid Malaysia_

covid countrylist - show the list of countries that can be checked
