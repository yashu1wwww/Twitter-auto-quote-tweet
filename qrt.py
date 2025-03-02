from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# List of Twitter accounts
accounts = [
    {"username": "john_doe123", "password": "Pass@1234"},
    {"username": "alice_smith99", "password": "Alice@456"},
    {"username": "michael_brown", "password": "Mike@789"}
]  # Add more accounts as needed

# Comments to post
commentsDict = [
    'good', 'amazing one', 'keep going', 'excellent', 'next video please', 'sub to your channel',
    'shared to others', 'made my day', 'keep it up', 'sensational', 'rock it', 'challenge it',
    'post video daily', 'work was amazing', 'needed more edit', 'edit was awesome', 'what a video man',
    'watched yesterday', 'you are genius', 'faster than light', 'your work needs success',
    'new fan of you', 'keep rocking dude', 'copy cat', 'link the video', 'listening', 'writing',
    'reading', 'playing'
]  

# Tweet URL to quote
tweet_url = "https://twitter.com/hasantoxr/status/1723266777705001004"  # Change this

# Number of quote tweets per account
num_quotes_per_account = 4  

for account in accounts:
    try:
        # Open a new browser for each account
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Open Twitter login page
        driver.get("https://twitter.com/i/flow/login")
        time.sleep(6)

        # Enter Username
        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "text")))
        email.send_keys(account["username"])
        email.send_keys(Keys.ENTER)
        time.sleep(2)

        # Enter Password
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        password.send_keys(account["password"])
        password.send_keys(Keys.ENTER)
        time.sleep(4)

        # Open the tweet to quote
        driver.get(tweet_url)
        time.sleep(5)

        # Quote tweet multiple times
        counter = 0
        while counter < num_quotes_per_account:
            try:
                # Click Retweet Button
                retweet_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='retweet']"))
                )
                retweet_button.click()
                time.sleep(1)

                # Click Quote Tweet Button
                quote_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Quote']"))
                )
                quote_button.click()
                time.sleep(1)

                # Enter Random Comment
                comment_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Post text']"))
                )
                comment_box.send_keys(random.choice(commentsDict))
                time.sleep(1)

                # Click Post Button
                post_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[text()="Post"]'))
                )
                post_button.click()
                time.sleep(1)

                counter += 1

            except Exception as e:
                print(f"Error while quoting tweet for {account['username']}: {e}")
                break

        # Close the browser after completing the task
        driver.quit()
        time.sleep(3)  # Small delay before switching to the next account

    except Exception as e:
        print(f"Error with account {account['username']}: {e}")

print("Task completed for all accounts.")
