import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

PATH = os.path.abspath('chromedriver')  # Con esto solucionamos el problema del PATH de cada uno


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)


driver.get("https://genius.com/#top-songs")
# print(driver.title)

tops = driver.find_element(By.ID,"top-songs")
songtainer = tops.find_element(By.CLASS_NAME,"PageGridFull-idpot7-0.jeWXO")

elements = songtainer.find_elements(By.TAG_NAME,"a")

songlist1=[]
for songstr in elements:
    song = (songstr.text).split("\n")
    type(song)
    song.remove("LYRICS")
    print(song)
    songlist1.append(song)




# driver.quit()