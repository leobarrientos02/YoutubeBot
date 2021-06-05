from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class YoutubeBot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def surf(self):
        bot = self.bot
        bot.get('https://www.youtube.com/')
        time.sleep(2)

    def search(self, video):
        bot = self.bot
        bot.get('https://www.youtube.com/results?search_query='+video)
        time.sleep(2)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(2,document.body.scrollHeight)')
            time.sleep(2)


video = input("Enter a video you want to see: ")

user = YoutubeBot()
user.surf()

user.search(video)
