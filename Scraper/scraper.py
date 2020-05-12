import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver import Chrome

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("Z:\mozilla downloads/chromedriver")

url = "https://www.yuvikaherbs.com/products/yuvika-multani-mitti-fullers-earth-multani-soil"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

dropdown = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[9]/div[1]/div/div/div[2]/span'
name = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[4]/div[1]/h1'
MRP = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[1]/span'
SP = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[2]'

product_name = driver.find_elements_by_xpath(name)[0].text
mrp = []
sp = []
weight = []

elem = driver.find_element_by_xpath(dropdown)
li = elem.find_elements_by_tag_name('option')

actions = ActionChains(driver)
actions.click(elem).perform()

for x in range(len(li)-1):
    time.sleep(1)
    li[x].click()
    weight.append(li[x].text)
    time.sleep(1)
    mrp.append(driver.find_element_by_xpath(MRP).text)
    sp.append(driver.find_element_by_xpath(SP).text)

product = {'Name': product_name, 'Weight': weight, 'MRP': mrp, 'SP': sp}
df = pd.DataFrame(product, columns=['Name', 'Weight', 'MRP', 'SP'])
print(df)
df.to_excel(r'Z:\details.xlsx', index=False, header=True)
