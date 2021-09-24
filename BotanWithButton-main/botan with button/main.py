import asyncio
import aiogram

from aiogram import Bot, Dispatcher, executor
from config import API_TOKEN
import csv, datetime, pymsql

loop = asyncio.get_event_loop()
bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
	from handlers import dp
	executor.start_polling(dp)

def statistics(user_id, command):
        data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
        with open('data.csv', 'a', newline="") as fil:
                wr = csv.writer(fil, delimiter=';')
                wr.writerow([data, user_id, command])
