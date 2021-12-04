
from time import sleep
from tqdm.contrib.telegram import tqdm
from functions import rawincount
from genBank import API_TOKEN, CHAT_ID
from telebot import TeleBot
from req import request
import io

fileName = 'generated2.txt'              # File for generated Patterns
telebot = TeleBot(API_TOKEN)
def smsg(messege):
    telebot.send_message(CHAT_ID, messege)
    pass
tempFile = io.StringIO('Potential usernames')
smsg(f'Preparing parsing, total variations: {rawincount(fileName)}')
with open(fileName, 'r') as f:
    print(f'Text file reached! ({fileName})')
    pbar = tqdm(f, total=rawincount(fileName), token=API_TOKEN, chat_id=CHAT_ID)
    for line in pbar:
        pbar.set_description(line)
        username = request(line[:-1])
        sleep(1)
        if username == True:
            print(line, file=tempFile)
            
telebot.send_document(CHAT_ID, data=tempFile)
# smsg('!DONE!')