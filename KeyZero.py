import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
driver.get('https://www.keyhero.com/free-typing-test')


sbutton = driver.find_element_by_class_name('start-button')

sbutton.click()

raw_input("Lets Start....")

quote = driver.find_element_by_class_name('quote')

keys = quote.text
print keys

search_box = driver.find_element_by_class_name('user-input-text')

for key in keys:
    search_box.send_keys(key)
    #time.sleep(.1)

search_box.submit()

raw_input("Quit....")

driver.quit()
