import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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
username.send_keys("sophiajewelryshop")
password.send_keys("K7!obFSboVG2mmW")
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
time.sleep(5)
b=driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Cargar más comentarios']")
b.click()

#Close Browser
time.sleep(5)
driver.close()