import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def post_to_instagram(path, username, password, photo, caption, share=True):
    option = webdriver.ChromeOptions()
    #option.add_argument("--start-maximized")
    cService = webdriver.ChromeService(executable_path='./chromedriver.exe', options=option)
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
    
    browser.find_element(By.NAME, 'username').send_keys(username)
    browser.find_element(By.NAME, 'password').send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    browser.find_element(By.XPATH, login_xpath).click()

    cred_save_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'
    wait.until(EC.element_to_be_clickable((By.XPATH, cred_save_xpath)))
    browser.find_element(By.XPATH, cred_save_xpath).click()

    time.sleep(5)

    notifications_xpath = '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
    wait.until(EC.element_to_be_clickable((By.XPATH, notifications_xpath)))
    browser.find_element(By.XPATH, notifications_xpath).click()

    new_post_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div/div[2]'
    wait.until(EC.element_to_be_clickable((By.XPATH, new_post_xpath)))
    browser.find_element(By.XPATH, new_post_xpath).click()

    select_file_xpath = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button'
    wait.until(EC.element_to_be_clickable((By.XPATH, select_file_xpath)))
    browser.find_element(By.XPATH, select_file_xpath).click()

    time.sleep(1)
    pyautogui.hotkey("ctrl", "6")
    pyautogui.typewrite(photo)
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(1)

    next_xpath = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div'
    wait.until(EC.element_to_be_clickable((By.XPATH, next_xpath)))
    browser.find_element(By.XPATH, next_xpath).click()

    next_nofilter_xpath = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div'
    wait.until(EC.element_to_be_clickable((By.XPATH, next_nofilter_xpath)))
    browser.find_element(By.XPATH, next_nofilter_xpath).click()

    textarea = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]'
    wait.until(EC.element_to_be_clickable((By.XPATH, textarea)))
    browser.find_element(By.XPATH, textarea).send_keys(caption)

    # Share!!!
    if share:
        share_xpath = "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div"
        wait.until(EC.element_to_be_clickable((By.XPATH, share_xpath)))
        browser.find_element(By.XPATH, share_xpath).click()
        time.sleep(120)
        browser.close()

if __name__ == "__main__":
    import sys

    username, password, photo, caption = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
    )
    post_to_instagram(username, password, photo, caption)