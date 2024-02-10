from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/')

driver.close() #close that particular tab
driver.quit() #close entire browser