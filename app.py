from selenium import webdriver
from selenium.webdriver.common import keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.Keys.RETURN)
        time.sleep(9)


    def likeTweets(self,hashtag):
        bot = self.bot    
        bot.get('https://twitter.com/search?q=%23'+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1,10):
            bot.find_element_by_xpath("//path[starts-with(@d, 'M')]").click()
            time.sleep(2)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)') 
            time.sleep(4)
      


    def postTweets(self,tweetBody):
        bot = self.bot    
        bot.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
        time.sleep(5) 
        body = tweetBody
        
        bot.find_element_by_class_name("notranslate").click()
        time.sleep(3)
        bot.find_element_by_class_name("notranslate").send_keys(body)
        time.sleep(5)
        bot.find_element_by_class_name("notranslate").send_keys(keys.Keys.ENTER)
        bot.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
        



pj = TwitterBot('Email', 'Password')


# pj.login()  --> To login

# pj.likeTweets('100DaysOfCode')  --> To like the tweets of particular hashtag

# pj.postTweets('My bot's first tweet!')  --> To post tweets

