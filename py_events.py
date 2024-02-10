from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')

events_dict = {i: {'name': events[i].find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0], 'time': events[i].find_element(By.TAG_NAME, 'a').text} for i in range(len(events))}

print(events_dict)