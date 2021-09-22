#%% Imports
from time import sleep
from types import prepare_class
from tqdm.contrib.telegram import tqdm
from driver import InstaBot, isAvailable
from functions import rawincount
from genBank import API_TOKEN, CHAT_ID
from telebot import TeleBot

fileName = 'generated2.txt'              # File for generated Patterns
telebot = TeleBot(API_TOKEN)
def smsg(messege):
    telebot.send_message(CHAT_ID, messege)
smsg(f'Preparing parsing, total varioations: {rawincount(fileName)}')
bot = InstaBot()
bot.chrome(True)
smsg('Chromedriver is Up')
try:
    bot.prepareChecks()
except:
    picture = bot.driver.get_screenshot_as_file('scr.png')
    img = open('scr.png', 'rb')
    telebot.send_photo(chat_id=CHAT_ID, photo=img)
    bot.driver.get('https://google.com/')
    sleep(2)
    picture = bot.driver.get_screenshot_as_file('scr.png')
    img = open('scr.png', 'rb')
    telebot.send_photo(chat_id=CHAT_ID, photo=img)
    pass
    bot.quit()
smsg('Instagram Reached')


smsg(f'Preparing parsing, total variations: {rawincount(fileName)}')
with open(fileName, 'r') as f:
    print(f'Text file reached! ({fileName})')
    pbar = tqdm(f, total=rawincount(fileName), token=API_TOKEN, chat_id=CHAT_ID)
    for line in pbar:
        pbar.set_description(line)
        username = isAvailable(bot.checkUser(line))
        sleep(0.3)
        if username == True:
            smsg(line)
smsg('!DONE!')
bot.quit()