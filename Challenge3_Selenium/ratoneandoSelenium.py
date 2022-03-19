import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

PATH = "C:\chromedriver.exe"

pagesDict = {
    "IntroPage": "Click on submit type",
    "Page1": "Click on Link",
    "Page2": "Click on Link",
    "Page3": "Click on Link",
    "Page4": "Click on Link",
    "Page5": "Click on Link",
    "Page6": "Click on Link",
    "Page7": "Click on Link",
    "Page8": "Click on Link",
    "Page9": "Find 9",
    "Page10": "Find 10",
    "Page11": "Find 11",
    "Page12": "Find 12",
    "Page13": "Find 13",
    "Page14": "Click on Link",
    "Page15": "Click on Link",
    "Page16": "Click on submit type",
    "Page17": "Click on submit type",
    "Page18": "Click on button submit type",
    "Page19": "Click on input image type",
    "Page20": "Click on Link",
    "Page21": "Click on Link",
    "Page22": "Click all table elements and continue",
    "Page23": "Find all buttons and then continue",
    "Page24": "Double Click on all then Continue",
    "Page25": "Drag and Drop Sliders and Continue",
    "Page26": "Click on Link",
    "Page27": "Click on Link",
    "Page28": "Click on Link",
    "Page29": "Click on Link",
    "Page30": "Click on Link",
    "Page31": "Click on Alert OK",
    "Page32": "Click on Link",
    "Page33": "Click all Checkboxes and Continue",
    "Page34": "Click on submit type",
    "Page35": "Click all Radios and Continue",
    "Page36": "Click on submit type",
    "Page37": "Select Cinco then Continue",
    "Page38": "Click on submit type",
    "Page39": "Select Seis then Continue",
    "Page40": "Click on submit type",
    "Page41": "Fill In Name and Lastname then Submit"
}

driver = webdriver.Chrome(executable_path=PATH)
driver.maximize_window()
#Open Website
driver.get('http://www.pbclibrary.org/raton/mousercise.htm')
for page in pagesDict:
    elements = []
    action = None
    alert_obj=None
    time.sleep(3)
    if pagesDict[page]=="Click on submit type":
        driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
        continue
    elif pagesDict[page]=="Click on Link":
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Find 9":
        driver.find_element(By.XPATH, "//a[contains(text(), '9')]").click()
        continue
    elif pagesDict[page]=="Find 10":
        driver.find_element(By.XPATH, "//a[contains(text(), '10')]").click()
        continue
    elif pagesDict[page]=="Find 11":
        driver.find_element(By.XPATH, "//a[contains(text(), '11')]").click()
        continue
    elif pagesDict[page]=="Find 12":
        driver.find_element(By.XPATH, "//a[contains(text(), '12')]").click()
        continue
    elif pagesDict[page]=="Find 13":
        driver.find_element(By.XPATH, "//a[contains(text(), '13')]").click()
        continue
    elif pagesDict[page]=="Click on button submit type":
        driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
        continue
    elif pagesDict[page]=="Click on input image type":
        driver.find_element(By.CSS_SELECTOR,"input[type='image']").click()
        continue
    elif pagesDict[page]=="Click all table elements and continue":
        elements = driver.find_elements(By.XPATH,"//td/img[@alt='botón']")
        for e in elements:
            time.sleep(1)
            e.click()
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Find all buttons and then continue":
        elements = driver.find_elements(By.CSS_SELECTOR, "input[type='button']")
        elements.append(driver.find_element(By.CSS_SELECTOR, "img[alt='flecha']"))
        elements.append(driver.find_element(By.CSS_SELECTOR, "img[alt='boton de inicio']"))
        elements.append(driver.find_element(By.CSS_SELECTOR, "img[alt='casa botón']"))
        elements.append(driver.find_element(By.CSS_SELECTOR, "img[alt='abrir']"))
        for e in elements:
            time.sleep(1)
            e.click()
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Double Click on all then Continue":
        elements = driver.find_elements(By.XPATH, "//td/img")
        action = ActionChains(driver)
        for e in elements:
            time.sleep(1)
            action.double_click(e).perform()
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Drag and Drop Sliders and Continue":
        elements = driver.find_elements(By.CSS_SELECTOR, "div[class='handle']")
        action = ActionChains(driver)
        for e in elements:
            time.sleep(1)
            action.drag_and_drop_by_offset(e,0,random.randint(-60,-6)).perform()
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Click on Alert OK":
        driver.find_element(By.TAG_NAME, 'a').click()
        time.sleep(2)
        alert_obj=driver.switch_to.alert
        alert_obj.accept()
        continue
    elif pagesDict[page]=="Click all Checkboxes and Continue":
        elements = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
        for e in elements:
            time.sleep(1)
            e.click()
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Click all Radios and Continue":
        elements = driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
        for e in elements:
            time.sleep(1)
            e.click()
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Select Cinco then Continue":
        selectElement = Select(driver.find_element(By.NAME,'theChoices'))
        selectElement.select_by_visible_text('Cinco')
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Select Seis then Continue":
        selectElement = Select(driver.find_element(By.NAME,'theChoices'))
        selectElement.select_by_visible_text('Seis')
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'a').click()
        continue
    elif pagesDict[page]=="Fill In Name and Lastname then Submit":
        nombre=driver.find_element(By.NAME,'fname')
        apellido=driver.find_element(By.NAME,'lname')
        nombre.clear()
        apellido.clear()
        nombre.send_keys("Joseph")
        apellido.send_keys("Gallardo")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
        continue
time.sleep(10)
driver.quit()
        
        
        
        
    
        
        
        
        
    
        
            
    
        
        
        
    