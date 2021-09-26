from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import *
import requests
import time
# import keyboard
from pynput.keyboard import Key, Controller

dic = {"Sa": ["+919792972971", "5%2000"],
       "Sarthak": ["9792972971", "5%2020"]}

driver = webdriver.Firefox()


def login():
    driver.get("https://web.whatsapp.com")
    time.sleep(8)


login()

lst = []

for name, numberSlot in dic.items():
    text1 = "Hi%20" + name
    text2 = '''%2C%20this%20is%20from%20%2APsych%20Club%2A%20%2C%20Manipal.%0AYour%20recruitment%20interview%20will%20be%20held%20on%20MS%20Teams%20.%20%0A%0A%0ADate%3A%2025th%20November%0ATime%3A%20'''
    text3 = '''pm%0A%0A%20We%20look%20forward%20to%20meeting%20you%21%20%0A%0A%28Kindly%20confirm%20your%20slot%29'''
    end_point = '''window.open("https://web.whatsapp.com/send?phone=%2B''' + \
        numberSlot[0] + "&text=" + text1 + text2 + \
        numberSlot[1] + text3+'''&app_absent=0");'''
    lst.append(end_point)

for url in lst:
    driver.execute_script(url)
    time.sleep(10)
    keyboard = Controller()
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)
    time.sleep(0.5)

time.sleep(0.5)
keyboard.press(Key.enter)
