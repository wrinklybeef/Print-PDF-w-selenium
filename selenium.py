from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from builtins import input

chromedriver_path = r'C:\Users\Adam\Downloads\chromedriver_win32\chromedriver'

service = Service(chromedriver_path)

service.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Chrome()

driver.get('')

username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'username'))
)

password_field = driver.find_element(By.NAME, 'password')

username_field.send_keys('')
password_field.send_keys('')

sign_in_button = WebDriverWait(driver, 1 0).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
)

sign_in_button.click()

time.sleep(10)


def click_download_button(driver, url):

    driver.get(url)

    # Find and click the download link
    download_link = driver.find_element(By.XPATH, "//a[contains(text(), 'PDF Report')]")
    download_link.click()

    time.sleep(5)


# List of URLs
url_list = [
]

for url in url_list:
    click_download_button(driver, url)

input("Press Enter when finished")
driver.quit()
service.stop()






