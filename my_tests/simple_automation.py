from pynput.mouse import Button, Controller  
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://youtube.com')

# You can put here your search
search_string = ('Still loving u')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys(search_string)

search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
search_button.click()
time.sleep(3)

# Mouse on video and click 1 time
mouse = Controller()
mouse.position = (234.50390625, 358.1171875) # Here make sure on your mouse position about video
time.sleep(2)
mouse.click(Button.left, 1)

# Skip ad
mouse.position = (716.265625, 558.109375) # Here make sure on your mouse position about 'skip ad'
time.sleep(7)
mouse.click(Button.left, 1)