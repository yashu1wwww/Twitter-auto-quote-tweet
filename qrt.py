import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("123_tweet") #replace with your twitter account & aslo replace in below where username asked
email.send_keys(Keys.ENTER)
time.sleep(2)
password = driver.find_element_by_name("password") #replace with your twitter password & also  replace in below where username asked
password.send_keys("pass1@#$")
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url) 

time.sleep(8)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"Somes tweet") #replace with your word do in below also..
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"true tweet")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"true tweeted now")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"best one")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"amazing")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.close()

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("123_tweet")
email.send_keys(Keys.ENTER)
time.sleep(2)
password = driver.find_element_by_name("password")
password.send_keys("pass1@#$")
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url) 

time.sleep(8)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"Somes tweet")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"true tweet")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"true tweeted now")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"best one")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"amazing")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.close()

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("123_tweet")
email.send_keys(Keys.ENTER)
time.sleep(2)
password = driver.find_element_by_name("password")
password.send_keys("pass@#$")
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url) 

time.sleep(8)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"Somes tweet")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"true tweet")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"true tweeted now")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"best one")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.implicitly_wait(4)
retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/a/div[2]/div/span').click()
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys(f"amazing")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click() 
driver.close()



