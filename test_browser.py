import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
cService = webdriver.ChromeService(executable_path='./chromedriver.exe', options=options)
driver = webdriver.Chrome(service = cService)
driver.get("https://www.ole.com.ar")
time.sleep(120)
wait = WebDriverWait(driver, 30)