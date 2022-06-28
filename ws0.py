from this import s
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

PATH = os.path.abspath('chromedriver')  

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

wait = WebDriverWait(driver, 10)

print("fetching page...")
driver.get("https://genius.com/#top-songs")

print(driver.title)
print("ok")
print("")

#En esta parte tocamos el botón de "Load More" 10 veces, si ocurre algun error se saltea esa parte y sigue adelante
count = 1
try:
    #1
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #2
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #3
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #4
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #5
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #6
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #7
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #8
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #9
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
    #10
    loadmore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='top-songs']/div/div[4]/div"))
    )
    print("pág.",count)
    print(loadmore.text)
    loadmore.click()
    count += 1
except:
    print("excepteado lince")
    pass


tops = driver.find_element(By.ID,"top-songs")
songtainer = tops.find_element(By.CLASS_NAME,"PageGridFull-idpot7-0.jeWXO")

elements = songtainer.find_elements(By.TAG_NAME,"a")

songlist1=[]
for songstr in elements:
    song = (songstr.text).split("\n") #convertimos el string a una lista
    song.remove("LYRICS") #le sacamos el elemento que contiene "LYRICS"
    if len(song) > 4:   #algunas canciones tienen un elemento mas que no nos interesa, lo removemos
        song.pop(3)
    print(song)
    songlist1.append(song)

    



# driver.quit()