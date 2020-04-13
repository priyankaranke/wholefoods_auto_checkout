from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from utils.secrets import EMAIL_ID, PWD
from utils.utils import get_decoded, send_email

# Load up chromedriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

# Log into amazon.com
driver.get("https://www.amazon.com")
driver.find_element_by_id("nav-link-accountList").click()

email_box = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ap_email"))
)
email_box.send_keys(get_decoded(EMAIL_ID))
email_box.submit()

password_box = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ap_password"))
)
password_box.send_keys(get_decoded(PWD))
password_box.submit()

# Go to cart
cart_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.ID, "nav-cart"))
)
cart_button.click()

#  then checkout
proceed_to_checkout_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.NAME, "proceedToALMCheckout-VUZHIFdob2xlIEZvb2Rz"))
)
proceed_to_checkout_button.click()

continue_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "a-autoid-0"))
)
continue_button.click()

subs_continue_button = WebDriverWait(driver, 7).until(
    EC.presence_of_element_located((By.ID, "subsContinueButton"))
)
subs_continue_button.click()

# Check if there are slots
no_slot_pattern = "No delivery windows available. New windows are released" + \
    " throughout the day."
no_slot_signal = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH,
            "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[1]/" +
            "div[4]/div[2]/div/div[3]/div/div/div/h4"))
)

if (no_slot_signal.text == no_slot_pattern):
    print("NO SLOTS!")
    send_email("Looks like no slots available right now :(")
else:
    print('SLOTS OPEN!')
    send_email("Looks like there is a slot! Go order now :)")
