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

# loadmore = driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div[2]/div/div[4]/div")
#loadmore = driver.find_element(By.CLASS_NAME,"SquareButton-sc-109lda7-0.gsoAZX")

maxclick = 9   #9
count = 1

# while count <= maxclick:
#     print(loadmore.text)
#     # loadmore.click()
#     count += 1
#     print("pag.",count)
#     time.sleep(3)


loadmore = driver.find_element(By.XPATH,"//*[@id='top-songs']/div/div[4]/div")
print(loadmore.text)
loadmore.click()

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