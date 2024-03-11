import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

authWindow = 0
ti12Window = 0
kunkaWindow = 0

timerKunka = 0
timerTI12 = 0

elementTI12 = 0
element = 0

bonusKunka = 0
bonusTI12 = 0

a = 1
tryingK = True
tryingT = True

options = webdriver.ChromeOptions()
options.add_argument('--headless')   
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def Main():
    global authWindow
    global kunkaWindow
    global ti12Window
    global timerKunka
    global timerTI12
    global tryingT
    global tryingK

    AuthInSteam()
    time.sleep(1)
    driver.switch_to.new_window()
    driver.get("https://epicloot.in/event")
    kunkaWindow = driver.current_window_handle
    driver.switch_to.new_window()
    driver.get("https://epicloot.in/theint")
    ti12Window = driver.current_window_handle
    driver.switch_to.window(authWindow)
    driver.close()

    print("Скрипт запущен. Проверка доступности подарка...")

    try:
        while a == 1:
            Claim_Kunka()
            Claim_TI12()
            if (tryingK == False or tryingT == False):
                if timerKunka > timerTI12:
                    print("Один/все из подарков в кд. Повторная проверка подарков через: ", timerKunka, "минут")
                    time.sleep(timerKunka * 60)
                else:
                    print("Один/все из подарков в кд. Повторная проверка подарков через: ", timerTI12, "минут")
                    time.sleep(timerTI12 * 60)
            else:
                print("Все подарки собраны! Проверка через 60 минут")
                time.sleep(3600)
    except:
        pass
    finally:
        print("Что то пошло не так, закрываю браузер и выхожу...")
        driver.switch_to.window(kunkaWindow)
        driver.close()
        driver.switch_to.window(ti12Window)
        driver.close()
        driver.quit()
        quit()
    

def Find_Element_Kunka():
    global kunkaWindow
    global element
    global timerKunka
    global tryingK

    try:
        wait = WebDriverWait(driver, timeout=3)
        element = driver.find_element(By.CLASS_NAME, 'game-gift__take')
        wait.until(lambda a : element.is_displayed())
        element.click()
        tryingK = True
    except:
        print("Подарок кунки забрать не получилось")
        timerKunka = 10
        tryingK = False
       

def Find_Enelemt_TI12():
    global ti12Window
    global elementTI12
    global timerTI12
    global tryingT

    try: 
        wait = WebDriverWait(driver, timeout=10)
        elementTI12 = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div/div[2]")
        wait.until(lambda a : elementTI12.is_displayed())
        elementTI12.click()
        time.sleep(1)
        elementTI12Case = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[3]")
        wait.until(lambda b : elementTI12Case.is_displayed())
        elementTI12Case.click()
        time.sleep(10)
        elementTI12Watch = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[4]/div[1]/div[1]")
        wait.until(lambda c : elementTI12Watch.is_displayed())
        elementTI12Watch.click()
        tryingT = True
    except:
        print("Подарок TI12 забрать не получилось")
        timerTI12 = 10
        tryingT = False


        

def Claim_Kunka():
    global bonusKunka
    global kunkaWindow
    global tryingK

    driver.switch_to.window(kunkaWindow)    
    driver.refresh()
    time.sleep(3)
    Find_Element_Kunka()
    if tryingK == True:
        bonusKunka += 1
        print('Бонус кунки забран! (' + (str(bonusKunka)) + ' шт)')
    

def Claim_TI12():
    global bonusTI12
    global ti12Window
    global tryingT

    driver.switch_to.window(ti12Window) 
    driver.refresh()
    time.sleep(3)
    Find_Enelemt_TI12()
    if (tryingT == True):
        bonusTI12 += 1
        print('Бонус TI12 забран! (' + (str(bonusTI12)) + ' шт)')

def Auth():
    global login
    global password
    try: 
        Auth = open('account/Auth.txt', 'r')
        if Auth.read() == "True":
            with open('account/login.txt') as fLogin:
                login = fLogin.read()
            with open('account/password.txt') as fPassword:
                password = fPassword.read()
            fPassword.close()
            fLogin.close()
        elif Auth.read == "False":
            print("Headless версия доступна только с автоматическим входом")
            print("Для изенения выбора удалите файл 'Auth' в папке 'account'")
            print("\nВыход из скрипта...")
            time.sleep(2)
            quit()
    except:
        Auth = open('account/Auth.txt', 'w')
        result = input("Включить автоматический вход в стим? (y/n): ")
        if (result == "y"):
            fLogin = open('account/login.txt', 'w') 
            fLogin.write(input("Напишите свой логин для автоматической авторизации: \n"))
            fPassword = open('account/password.txt', 'w') 
            fPassword.write(input("Напишите свой пароль: "))
            fLogin.close()
            fPassword.close()
            fLogin = open('account/login.txt', 'r')
            fPassword = open('account/password.txt', 'r') 
            login = fLogin.read()
            password = fPassword.read()
            fPassword.close()
            fLogin.close()
            Auth = open('account/Auth.txt', 'w')
            Auth.write("True")
            Auth.close()
            print("Для изенения выбора удалите файл 'Auth' в папке 'account'")
            print('')
        elif (result == "n"): 
            Auth = open('account/Auth.txt', 'w')
            Auth.write("False")
            Auth.close()
            print("Headless версия доступна только с автоматическим входом")
            print("Для изенения выбора удалите файл 'Auth' в папке 'account'")
            print('')
            print("Выход из скрипта...")
            time.sleep(2)
            quit()

def AuthInSteam():
    global login
    global password
    wait = WebDriverWait(driver, timeout=20)
    sButton = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div[3]/div/a[2]")
    wait.until(lambda a : sButton.is_displayed())
    sButton.click()
    time.sleep(5)
    loginPrint = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input")
    wait.until(lambda b : loginPrint.is_displayed())
    loginPrint.click()
    loginPrint.send_keys(str(login))
    passwordPrint = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input")
    wait.until(lambda c : passwordPrint.is_displayed())
    passwordPrint.click()
    passwordPrint.send_keys(str(password))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button").click()
    time.sleep(2)
    print("Подтвертие вход в аккаунт в вашем 'Steam Guard'")
    input("Если у вас его нет, или вы уже вошли в аккаунт, нажмите Enter \n")
    os.system('cls')
    print ("EpicLoot 'Event-Claimer'")
    print("Headless experemental version (silent)\n")
    try:
        time.sleep(7)
        finalAuth = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div/div[2]/div[2]/div/form/input[5]")
        wait.until(lambda d : finalAuth.is_displayed())
        finalAuth.click()
    except:
        print("\n")
        print("Вход прошел с ошибкой. Свяжитесь со мной!")
        input()
        quit()



##start
print("EpicLoot 'Event-Claimer'")
print("Headless experemental version (silent)\n")
Auth()
print("Вы включили headless версию. В ней проверка доступности подарка не доступна\n"
      "Проверка будет происходить каждые 10 минут, если один из подарков не доступен\n"
      "Отличительная особенность этой версии: браузер не будет открыватся. Все действия будут проходить в silent режиме\n"
      "Если с этим режимом возникают проблемы, то перейдите на обычную версию\n")
print("headless версия - эксперементальная. В может быть много багов\n"
      "Одни из них: черезвычайная нагрузка на CPU и возможность закрыть браузер только через диспетчер задач\n")
input("Нажмите Enter: ")
driver = webdriver.Chrome(options=options)
driver.get('https://epicloot.in/')
authWindow = driver.current_window_handle
time.sleep(0.25)

Main()