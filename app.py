from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class TwitterBot:
    def __init__(self,username,password,hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag
        self.webBot = webdriver.Firefox()
        webdriver.Firefox()

    def login(self):
        bot = self.webBot
        bot.get("https://twitter.com/login")
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def likeTweets(self):
        bot = self.webBot
        bot.get('https://twitter.com/search?q='+self.hashtag+'&src=typed_query')
        time.sleep(4)
        for i in range(1,100):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(4)
            tweets = bot.find_elements_by_xpath("//a[@dir ='auto']")
            links = [elem.get_attribute('href') for elem in tweets]
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_css_selector(
                        '.css-18t94o4[data-testid ="like"]'
                    ).click()
                    print('tweet liked')
                    time.sleep(30)
                except Exception as ex:
                    time.sleep(2)



bot1 = TwitterBot(input("Enter your twitter email: "),input("Enter your password: "),input("Enter a hashtag #"))
bot1.login()
bot1.likeTweets()
