import time
from selenium import webdriver

PATH = "C:\chromedriver.exe"
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(executable_path=PATH,chrome_options=chrome_opt)
driver.maximize_window()
driver.get('https://www.instagram.com/p/B166OkVBPJR/')
time.sleep(3)
driver.close()