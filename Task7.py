import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
service = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window
driver.maximize_window()
driver.get("https://userinyerface.com/game.html")
block = driver.find_element(By.CSS_SELECTOR, '#app .game .cookies')
# Bloğun yüksekliğini kontrol et
block_height = block.size['height']
print(f"Blok yüksekliği: {block_height}px")
# Bloğun arka plan rengini kontrol et
block_background_color = block.value_of_css_property('background-color')
print(f"Bloğun arka plan rengi: {block_background_color}")