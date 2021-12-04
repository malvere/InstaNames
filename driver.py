from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
import genBank
# ChromeDriver Options
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument(genBank.USER_AGENT)


# Bot Functions and Controlls:
class InstaBot():
    def __init__(self):
        pass

    # Init Safaridriver
    def safari(self):
        self.driver = webdriver.Safari()

    # Init Chromedriver
    def chrome(self, headless):
        options.headless = headless
        self.driver = webdriver.Chrome(options=options)

    # If is being runned on heroku
    def heroku(self):
        import os
        options.headless = True
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.driver = webdriver.Chrome(
            executable_path=os.environ.get(
                "CHROMEDRIVER_PATH"), options=options)

    def prepareChecks(self):
        print('Connecting to Instagram')
        self.driver.get('https://www.instagram.com/accounts/emailsignup/')
        sleep(3)
        self.driver.find_element_by_name(
            'emailOrPhone').send_keys('vain@glory.com')
        self.driver.find_element_by_name('password').send_keys('qwerty')
        print('Done')

    def checkUser(self, username):
        inputForm = self.driver.find_element_by_name('username')
        inputForm.send_keys(username)
        # inputForm.send_keys(Keys.RETURN)
        self.driver.find_element_by_class_name('XFYOY').submit()
        sleep(0.6)
        try:
            # 'Это имя пользователя уже занято. Попробуйте другое.'
            userStatus = self.driver.find_element_by_id('ssfErrorAlert').text
        except Exception:
            sleep(3)
            # 'Это имя пользователя уже занято. Попробуйте другое.'
            userStatus = self.driver.find_element_by_xpath(
                '//*[@id="ssfErrorAlert"]').text
        for i in range(len(username)):
            inputForm.send_keys(Keys.BACKSPACE)
        return userStatus

    # Quits Driver
    def quit(self):
        self.driver.quit()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as ec
        from selenium.webdriver.common.by import By
        login = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.NAME, 'username')))
        self.driver.find_element_by_name(
            'password').send_keys(genBank.PASSWORD)
        sleep(0.2)
        login.send_keys(genBank.EMAIL)
        self.driver.find_element_by_id(
            'loginForm').submit()

    def preCheck(self, username):
        # ---------------------------------------------
        # Runs a Pre-Check which determines
        # if username is claimed or cloud be obtainable
        # ---------------------------------------------
        self.driver.get(f'https://www.instagram.com/{username}/channel/?__a=1')
        page = self.driver.find_element_by_tag_name('body').text
        if page == '{}':
            return True                 # Username is Claimable or Black-listed
        else:
            return False                # Username is Taken


# Checks Function
def isAvailable(status):
    if (
        status == "This username isn't available. Please try another." or
        status == "Это имя пользователя уже занято. Попробуйте другое."
            ):
        return False
    elif (
            status == "Create a password at least 6 characters long."
            or status == "Очень простой пароль. Создайте новый."
            or status == "Похоже, вы неверно указали номер телефона. Введите полный номер с кодом страны."
            or status == "This password is too easy to guess. Please create a new one."
                ):
        return True
