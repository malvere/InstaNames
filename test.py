
from time import sleep
from telebot import TeleBot, types
from genBank import API_TOKEN, CHAT_ID
from tqdm.contrib.telegram import trange, tqdm
from functions import rawincount

telebot = TeleBot(API_TOKEN)
telebot.remove_webhook()
telebot.send_message(CHAT_ID, 'HI')

fileName = 'generated2.txt'
@telebot.message_handler(commands=['start'])
def start_message(message):
    if CHAT_ID != message.chat.id:
        telebot.send_message(message.chat.id, 'Запускаюсь, готов к работе.', reply_markup=None)
        for i in trange(10, token=API_TOKEN, chat_id=CHAT_ID):
            sleep(1)
            pass
    else:
        telebot.send_message(message.chat.id, f'!!DENIED!! {message.chat.id}')

@telebot.message_handler(commands=['tqdm'])
def start_message(message):
    if CHAT_ID != message.chat.id:
        telebot.send_message(message.chat.id, 'Запускаюсь, готов к работе.', reply_markup=None)
        with open(fileName, 'r') as f:
            print(f'Text file reached! ({fileName})')
            pbar = tqdm(f, total=rawincount(fileName), token=API_TOKEN, chat_id=CHAT_ID)
            for char in pbar:
                pbar.set_description(char)
                sleep(1)
        # pbar = tqdm(["a", "b", "c", "d"], token=API_TOKEN, chat_id=CHAT_ID, total=30)
        # for char in pbar:
        #     sleep(1)
        #     pbar.set_description("Processing %s" % char)
        #     pass
    else:
        telebot.send_message(message.chat.id, f'!!DENIED!! {message.chat.id}')

telebot.polling()