from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import time
path_profile = r'C:\\Users\\Vaibhav\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\nchscwx1.Selenium'
options = Options()
options.add_argument("--headless-new")
options.profile = path_profile
browser = webdriver.Firefox(options=options)
browser.get('https://x.com/home')
"""def login_fun(): 
    time.sleep(3)
    user_fill = browser.find_element(By.CSS_SELECTOR, 'input[name="text"]')
    user_fill.click()
    user_fill.send_keys('covix2772')
    next_button = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
    next_button.click() 
    time.sleep(3)
    pass_fill = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    pass_fill.click()
    pass_fill.send_keys('Tityboi@123') 
    time.sleep(3)
    loginbutton = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
    loginbutton.click()
    time.sleep(3)
    wait = WebDriverWait(browser, 10)
    browser.get('https://x.com/compose/post')"""
browser.implicitly_wait(3)
def login_send_tweet(message): 
    #time.sleep(3)
    try: 
        tweetButton = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        #time.sleep(3)
        tweetButton.click()
        #time.sleep(3)
        textBox = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        textBox.click()
        #time.sleep(3)
        textBox.send_keys(message)
        #time.sleep(3)
        postButton = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        postButton.click()
        messagebox.showinfo("Success", "Tweet posted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to post tweet: {e}")
