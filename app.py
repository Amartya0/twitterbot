from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class twitterbot:
    def __init__(self, username, password, hashatag):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(3)
        email= bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)



aj=twitterbot('optimisticbot5', 'twitterbot123',)
aj.login()

