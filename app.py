import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from libs.ADB import ADB
from libs.FakeMail import FakeMail

adb = ADB()
adb.devices()
fakemail = FakeMail()

adb.aeroplane(1)
time.sleep(5)
adb.aeroplane(0)
time.sleep(6)
adb.hotspot(1)
adb.connectWifi('Redmi', '00000000')

exit()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://facebook.com')

get_email = fakemail.email()

if get_email.get('status') == 'success':
    email = get_email.get('email')
    mobile = str(randint(8, 9)) + str(randint(7, 9)) + str(
        randint(55, 99)) + str(randint(111111, 999999))
    password = email[:-1]

    WebDriverWait(browser, 20).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a')))

    create = browser.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()

    WebDriverWait(browser, 20).until(EC.presence_of_element_located(
        (
            By.XPATH,
            '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input')))

    first_name = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input')
    first_name.send_keys('Popi')
    time.sleep(2)

    last_name = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input')
    last_name.send_keys('Biswas')

    mobile_box = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input')
    mobile_box.send_keys(mobile)
    time.sleep(2)

    password_box = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input')
    password_box.send_keys(password)
    time.sleep(2)

    dd = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]')
    dd.send_keys('10')
    time.sleep(2)

    mm = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]')
    mm.send_keys('10')
    time.sleep(2)

    yy = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]')
    yy.send_keys('1991')
    time.sleep(2)

    gender = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input')
    gender.click()
    time.sleep(2)

    button = browser.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[10]/button')
    button.click()

    try:
        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/a')))

        update = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/a')
        update.click()

        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[5]/div[2]/div/div/form/div[2]/div/div/input')))

        email_box = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/form/div[2]/div/div/input')
        email_box.send_keys(email)

        add = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/form/div[3]/button')
        add.click()

        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input')))

        while True:
            message = fakemail.messages(email)

            if message.get('status') == 'success':
                otp = message.get('otp')
                break

        code_box = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input')
        code_box.send_keys(otp)

        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/button')))

        email_submit = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/button')
        email_submit.click()

        print('Email -' + email + ', Password - ' + password)

        time.sleep(10)
        browser.quit()

    except:

        browser.quit()
        print('Account checkpointed !!')

else:

    browser.quit()
    print('Unable to get email address !!')
