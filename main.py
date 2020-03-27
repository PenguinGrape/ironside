import sys
import time
import telebot
from telebot import types

API_TOKEN = '<TOKEN>'

bot = telebot.TeleBot(API_TOKEN)
# it works only for my bot, lol, change it
voice_id = 'AwACAgIAAxkDAAMGXn4SSST4GuQN9x0WrdNe4qdecqIAAv8GAAIY8vBLsl1uvq8rdYkYBA'


@bot.inline_handler(lambda query: query.query == '')
def query_text(inline_query):
    r = types.InlineQueryResultCachedVoice('1', voice_file_id=voice_id, title='Ironside')
    bot.answer_inline_query(inline_query.id, [r])


def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
