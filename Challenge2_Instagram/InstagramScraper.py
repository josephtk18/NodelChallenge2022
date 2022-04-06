from ast import While
from asyncio.windows_events import NULL
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

#This file uses Selelinum to automate the process of recording raw network traffic from the instagram post 
# comments request to parse them later
PATH = "C:\chromedriver.exe"
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(executable_path=PATH,chrome_options=chrome_opt)
driver.maximize_window()
#Open Instagram
driver.get('https://www.instagram.com')

#Login
time.sleep(5)
username=driver.find_element_by_css_selector("input[name='username']")
password=driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("***********")#Use your instagram account credentials
password.send_keys("***********")#Don't use your main account
login = driver.find_element_by_css_selector("button[type='submit']").click()

#save your login info?
time.sleep(5)
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]").click()
#turn on notif
time.sleep(5)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]").click()

#Once inside, get to the post
time.sleep(5)
driver.get('https://www.instagram.com/p/B166OkVBPJR/')
#click on More Comments button
time.sleep(10)
b=driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Cargar más comentarios']")
while b:
    childComments = driver.find_elements(By.XPATH,"//span[contains(text(), 'Ver respuestas ')]")
    for c in childComments:
        time.sleep(3)
        c.click()
    childComments = None
    time.sleep(5)
    b.click()
    time.sleep(10)
    try:
        b=driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Cargar más comentarios']")
    except NoSuchElementException:
        b=None
else:
    print("No more comments to load...")

#Close Browser
time.sleep(5)
print("Please download .har file from Chrome dev tools window and parse it into a json file with all the comments for the post...")
##driver.close()