from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class PofBot():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://pof.com')

    sleep(2)

    accpet_cookies = driver.find_element('xpath', '/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[1]')
    accpet_cookies.click()

    sleep(2)


    signIn = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/header/nav/ul/li[1]/a')
    signIn.click()

    sleep(2)

    username = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/form/div[2]/div[1]/label/div/input')
    username.click()
    username.send_keys('kenniealfonz@gmail.com')

    password = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/form/div[2]/div[2]/label/div/input')
    password.click()
    password.send_keys('WhateverThisIs!')

    login = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/form/div[3]/button')
    login.click()

    sleep(3)
    
    closePopUp = driver.find_element('xpath', '/html/body/div[4]/div[3]/div/div/div/div[2]/button')
    closePopUp.click()

    

    closePopUp2 = driver.find_element('xpath', '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div/a')
    closePopUp2.click()

    meetMe = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div[2]/div/nav/div/ul/li[2]/a/span/h1/span')
    meetMe.click()

    sleep(2)

    while True:
        sleep(3)
        try:
            likeButton = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[10]/div[2]/div/div/div[4]/button')
            likeButton.click()
        except:
            print("failed attempt")
            

bot = PofBot()
