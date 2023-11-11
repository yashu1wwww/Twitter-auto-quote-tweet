from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(6)
email = driver.find_element_by_name('text')
email.send_keys("FUser73216") #replace with your twitter account username
email.send_keys(Keys.ENTER)
time.sleep(2)
password = driver.find_element_by_name("password") #replace with your twitter password 
password.send_keys("Twitter_123")
password.send_keys(Keys.ENTER)
time.sleep(4)
driver.get("https://twitter.com/Kannada_KBO_/status/1723223451043799453") #replace with which post you want auto quote..
time.sleep(5)

counter = 0
while True:
    try:
        
        # Post the tweet
        driver.find_element_by_xpath("//div[@data-testid='retweet']/div").click() #retweet button
        time.sleep(1)
        #click on quote button
        driver.execute_script('document.querySelector("#layers > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div:nth-child(2) > div > div.css-1dbjc4n.r-14lw9ot.r-1q9bdsx.r-1upvrn0.r-j2cz3j.r-1udh08x.r-u8s1d > div > div > div > a:nth-child(2) > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > span").click()')
        time.sleep(1)
        driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(random.choice(commentsDict)) #randomly cmt
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span').click() #click on post button
        time.sleep(1)  

           
        counter += 1
        if counter == 4: #Change '5' to 'how many auto tweet for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
