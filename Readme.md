# InstaNames
This is a Selenium version of Instagram parser  
Used to determine valid Instagram IDs by passing potential usernames from [AIOP Bot](https://github.com/malvere/AIOPostgresBot)  

[![Python](https://img.shields.io/badge/Python-3.9-yellowgreen)](https://www.python.org)
[![Selenium](https://img.shields.io/badge/-Selenium-green)](https://docs.python-requests.org/en/latest/)
[![Telebot](https://img.shields.io/badge/-telebot-lightblue)](https://github.com/aiogram/aiogram)

## Features
- Uses Selenium and custom UserAgent to parse IDs into Instagram's registration form
- Uses Telebot library to implement Bot controls and notifications via Telegram
- Supports Cloud-Platforms in Headless mode 
- Determines if username is banned or valid

## Notes
For proper work on Cloud-Platforms needs proxy to hide enterprise IP address and avoid login page redirect in Instagram
