 #twitter bot updated with the recent login format of Twitter
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"FileAddressHere"
driver= webdriver.Chrome()

#login
driver.get("https://www.twitter.com/login")
driver.implicitly_wait(10)

#email
email_xpath='//input[@name="username"]'
email=driver.find_element_by_xpath(email_xpath)
email.send_keys('youremailhere')
email.send_keys(Keys.RETURN)


#password
password_xpath='//input[@name="password"]'
password=driver.find_element_by_xpath(password_xpath)
password.send_keys('yourpasswordhere')
password.send_keys(Keys.RETURN)


n=10
loopn=100
#any number you like 100 is a joke

#tweet loop
for i in range(loopn):
   
    message=driver.find_element_by_xpath(message_xpath)
    message.send_keys("Your Text Here")
    tweet_xpath='//*[@data-testid="tweetButtonInline"]'
    tweet=driver.find_element_by_xpath(tweet_xpath)
    time.sleep(10)
    tweet.click()
    time.sleep(n)
    #increasing sleep time by 10 so that it does not get banned
    n=n+10
    i=i+1
