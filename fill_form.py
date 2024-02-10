from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://secure-retreat-92358.herokuapp.com/')

driver.find_element(By.NAME, 'fName').send_keys('Awwab')
driver.find_element(By.NAME, 'lName').send_keys('Khan')
driver.find_element(By.NAME, 'email').send_keys('awwabkhan@gmail.com')
driver.find_element(By.TAG_NAME, 'button').click()
