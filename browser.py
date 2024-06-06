import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

current_path = os.path.dirname(os.path.abspath(__file__))

def check_exists_by_xpath(browser, xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class(browser, class_name):
    try:
        browser.find_element(By.CLASS_NAME, class_name)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_text(browser, text):
    try:
        browser.find_element(By.LINK_TEXT, text)
    except NoSuchElementException:
        return False
    return True 

def post_to_instagram(path, username, password, photo, caption, filename, logger, root):
    logger.info("Setting up browser session...")
    option = webdriver.ChromeOptions()
    cService = webdriver.ChromeService(executable_path='./asset/chromedriver.exe', options=option)
    browser = webdriver.Chrome(service=cService, options=option)
    browser.set_window_position(0, 0)
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    browser.get("https://www.instagram.com")
    wait = WebDriverWait(browser, 30)
  
    username_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    login_xpath = '//*[@id="loginForm"]/div/div[3]'

    wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    
    time.sleep(2)
    logger.info("Logging in Instagram")
    browser.find_element(By.NAME, 'username').send_keys(username)
    browser.find_element(By.NAME, 'password').send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    browser.find_element(By.XPATH, login_xpath).click()
    logger.info("Login successful")

    cred_save_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'
    wait.until(EC.element_to_be_clickable((By.XPATH, cred_save_xpath)))
    browser.find_element(By.XPATH, cred_save_xpath).click()

    #time.sleep(120)

    notifications_xpath = '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
    wait.until(EC.element_to_be_clickable((By.XPATH, notifications_xpath)))
    browser.find_element(By.XPATH, notifications_xpath).click()

    logger.info("Creating new post")
    new_post_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div/div[2]'
    wait.until(EC.element_to_be_clickable((By.XPATH, new_post_xpath)))
    browser.find_element(By.XPATH, new_post_xpath).click()

    post_full_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/div/div/div[1]/a[1]/div[1]/div/div/div[1]/div/div/span/span'
    if check_exists_by_xpath(browser, post_full_xpath):
        logger.info("Choosing post")
        wait.until(EC.element_to_be_clickable((By.XPATH, post_full_xpath)))
        browser.find_element(By.XPATH, post_full_xpath).click()

    logger.info("Selecting the file to uplaod")
    select_file_xpath = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button'
    wait.until(EC.element_to_be_clickable((By.XPATH, select_file_xpath)))
    browser.find_element(By.XPATH, select_file_xpath).click()
    
    time.sleep(1)
    pyautogui.hotkey("ctrl", "6")
    pyautogui.typewrite(photo)
    time.sleep(2)
    pyautogui.hotkey("enter")
    time.sleep(20)

    logger.info("File uploaded successfully")
    reel_xpath = '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button'
        
    if check_exists_by_xpath(browser, reel_xpath):
        logger.info("Reel popup was caught, I better accept it")
        browser.find_element(By.XPATH, reel_xpath).click()

    reel_cover_class = 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37'
    time.sleep(2)
    if check_exists_by_class(browser, reel_cover_class):
        logger.info("Choosing Reel Cover")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, reel_cover_class)))
        browser.find_element(By.CLASS_NAME, reel_cover_class).click()

    next_xpath = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div'
    wait.until(EC.element_to_be_clickable((By.XPATH, next_xpath)))
    browser.find_element(By.XPATH, next_xpath).click()

    next_nofilter_xpath = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div'
    wait.until(EC.element_to_be_clickable((By.XPATH, next_nofilter_xpath)))
    browser.find_element(By.XPATH, next_nofilter_xpath).click()

    textarea = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]'
    wait.until(EC.element_to_be_clickable((By.XPATH, textarea)))
    browser.find_element(By.XPATH, textarea).send_keys(caption)

    share_xpath = "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div"
    wait.until(EC.element_to_be_clickable((By.XPATH, share_xpath)))
    browser.find_element(By.XPATH, share_xpath).click()
    time.sleep(60)
    logger.info("Content posted successfully")
    browser.close()
    browser.quit()
    logger.info("##### Finished " + filename + " #####")
    root.destroy()