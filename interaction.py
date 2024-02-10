from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# scraping article count
# articlecount_parent = driver.find_element(By.ID, 'articlecount')
# article_count = articlecount_parent.find_element(By.TAG_NAME, 'a')
# print(article_count.text)

# article_count.click()

# interacting with wikipedia
# searching through search bar
search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys('Python', Keys.ENTER)