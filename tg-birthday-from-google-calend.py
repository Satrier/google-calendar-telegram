# pip install asyncio datetime os random re time python-telegram-bot google-auth google-api-python-client openai python-dotenv

import asyncio
import datetime
import os
import random
import re
import time
import telegram
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import openai
from dotenv import load_dotenv
load_dotenv()


# Set your own values in the variables below and #60 .json file path/ Встановіть власні значення у змінні нижче та #60 строка шлях до .json файлу
GOOGLE_CALENDAR_ID = 'PUT_HERE_your_google_calendae_id@group.calendar.google.com'
TELEGRAM_BOT_TOKEN = 'PUT_HERE_your_telegram_token'
# group like https://api.telegram.org/bot451456154:Affdsef-MdF-Hf89-4_ZXdfif7hnok/getUpdates
#chanell 
TELEGRAM_GROUP_CHAT_ID = '-12345678945612' #or group '123456789'
OPENAI_API_KEY = os.getenv("HERE")

openai.api_key = "PUT_HERE" #is paid

async def get_greetings(name: str, description: str) -> str:
    """
    Generating greetings using OpenAI API / Генерація поздоровлення за допомогою OpenAI API
    """
    prompt = f"Generate greetings from colleagues for {name} on National Day with honors from 40-50 words and a line of words about {description}, then add the Emoji Telegram line to the text of the notification." \
             f"Some notes" 
    while True:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                #engine="gpt-4", #not yet
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                timeout=120,
                temperature=0.7,
                top_p=1,
                best_of=3
            )

            message = response.choices[0].text.strip()
            message = re.sub(r"\n+", "\n", message)
            return message
        #except openai.error.APIError:
        except (openai.error.ServiceUnavailableError, openai.error.APIError, openai.error.RateLimitError):
            print("API Error occurred. Waiting for 20 minutes and trying again...")
            time.sleep(1200)

def get_events_today() -> list:
    """
    Get today's events from Google Calendar / Отримання подій сьогодні з Google Календаря
    """
    credentials = Credentials.from_service_account_file(
        "/home/user/file-from-calendar.json",
        scopes=["https://www.googleapis.com/auth/calendar.readonly"],
    )
    service = build("calendar", "v3", credentials=credentials)
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    today = datetime.datetime.now().date()
    events_result = (
        service.events()
        .list(
            calendarId=GOOGLE_CALENDAR_ID,
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    today_events = []
    if not events:
        print("No events found.")
    for event in events:
        start = event["start"].get("date")
        if start == today.strftime("%Y-%m-%d"):
            today_events.append(event)

    return today_events

async def send_telegram_message(message: str) -> None:
    """
    Sending a message to a Telegram group / Надсилання повідомлення до Telegram групи
    """
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_GROUP_CHAT_ID, text=message, parse_mode='Markdown')


async def main() -> None:
    events_today = get_events_today()
    if events_today:
        message = f"Hello everyone 👋 Today we wish you a happy birthday: "
        for event in events_today:
            name = event["summary"]
            description = event.get("description", "")
            greetings = await get_greetings(name, description)
            message += f"\n🎈*{name}* !) 🥳🎉\n{greetings}"

        await send_telegram_message(message)
    else:
        print("There are no birth events today")

if __name__ == '__main__':
    asyncio.run(main())
