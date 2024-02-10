from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/Learning-Python-Second-Fran%C3%A7ois-Chollet/dp/1617296864/ref=sr_1_1?crid=J1V151KWX9ZL')

price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
fraction = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text
print(f"The price is {price}.{fraction}")
# driver.close() #close that particular tab
# driver.quit() #close entire browser