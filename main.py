import requests
import os
from datetime import date, timedelta
from twilio.rest import Client
from tkinter import *


DAYS_SINCE_LAST_TRADING_DAY = ""
DAYS_SINCE_DAY_BEFORE_LAST_TRADING_DAY = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("alpha_vantage_api_key")
NEWS_API_KEY = os.environ.get("news_api_key")
TWILIO_ACCOUNT_SID = os.environ.get("account_sid")
TWILIO_AUTH_TOKEN = os.environ.get("auth_token")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
THEME_COLOR = "#202020"
window = Tk()
window.title("Stock News Notifier")
window.config(padx=20, pady=20, bg=THEME_COLOR)
window.mainloop()

alpha_params ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# Check for which day of week it is
# def check_day():
#     global DAYS_SINCE_LAST_TRADING_DAY, DAYS_SINCE_DAY_BEFORE_LAST_TRADING_DAY
#     now = date.today()
#
#     if now.weekday() == 6: #if sunday get Fri Close and Thurs Close
#         days_since_last_trading_day = 2
#         days_since_day_before_last_trading_day = 3
#     elif now.weekday() == 5: #if saturday get Fri Close and Thurs Close
#         days_since_last_trading_day = 1
#         days_since_day_before_last_trading_day = 2
#     elif now.weekday() == 0: #if monday get Mon Close and Fri CLose
#         days_since_last_trading_day = 0
#         days_since_day_before_last_trading_day = 3
#     else:
#         days_since_last_trading_day = 0
#         days_since_day_before_last_trading_day = 1
#
#     DAYS_SINCE_LAST_TRADING_DAY = str(now - timedelta(days=days_since_last_trading_day))
#     DAYS_SINCE_DAY_BEFORE_LAST_TRADING_DAY = str(now - timedelta(days=days_since_day_before_last_trading_day))
#
#     return DAYS_SINCE_LAST_TRADING_DAY, DAYS_SINCE_DAY_BEFORE_LAST_TRADING_DAY
#
#
#
#
# check_day()
# stock_response = requests.get(STOCK_ENDPOINT, params= alpha_params)
# stock_response.raise_for_status()
# stock_data = stock_response.json()
# yesterday_closing = float(stock_data["Time Series (Daily)"][DAYS_SINCE_LAST_TRADING_DAY]["4. close"])
# day_before_yesterday_closing = float(stock_data["Time Series (Daily)"][DAYS_SINCE_DAY_BEFORE_LAST_TRADING_DAY]["4. close"])
#
# difference = yesterday_closing - day_before_yesterday_closing
# print(difference)
# up_down = None
# if difference > 0:
#     up_down = "🔼"
# else:
#     up_down = "🔽"
# percentage_difference = round((difference / yesterday_closing) * 100)

# if abs(percentage_difference) >= 4:
#     news_params = {
#         "apiKey": NEWS_API_KEY,
#         "qInTitle": COMPANY_NAME,
#         "language": "en",
#
#     }
#     news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
#     articles = news_response.json()["articles"]
#     num_of_articles = articles[:1]
#
#
#     formatted_articles = [f"{STOCK_NAME}: {up_down}{abs(percentage_difference)}%\nHeadline: {article['title']}.\nBrief:{article['description']}" for article in num_of_articles]
#
#     print(formatted_articles)
#
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#
#     for article in formatted_articles:
#         message=client.messages \
#             .create(
#             body=article,
#             from_="+18548889151",
#             to="+18582088079"
#             )
#         print(message.status)

