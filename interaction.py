from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

articlecount_parent = driver.find_element(By.ID, 'articlecount')
article_count = articlecount_parent.find_element(By.TAG_NAME, 'a').text
print(article_count)