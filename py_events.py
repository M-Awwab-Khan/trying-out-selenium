from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')

events_dict = {}

i=0
for event in events:
    events_dict[i] = {
        'time': event.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0],
        'name': event.find_element(By.TAG_NAME, 'a').text
    }
    i += 1

print(events_dict)