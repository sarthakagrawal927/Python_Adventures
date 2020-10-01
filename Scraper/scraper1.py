from selenium.common.exceptions import StaleElementReferenceException
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("Z:\mozilla downloads/chromedriver")

product_name = []
mrp = []
sp = []
weight = []


def work(url):
    try:
        driver.get(url)
        time.sleep(1)

        dropdown = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[9]/div[1]/div/div/div[2]/span'
        name = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[4]/div[1]/h1'
        MRP = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[1]/span'
        SP = '/html/body/section/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[2]'

        elem = driver.find_element_by_xpath(dropdown)
        li = elem.find_elements_by_tag_name('option')

        actions = ActionChains(driver)
        actions.click(elem).perform()

        for x in range(len(li)):
            time.sleep(0.2)
            li[x].click()
            weight.append(li[x].text)
            time.sleep(0.2)
            product_name.append(driver.find_elements_by_xpath(name)[0].text)
            mrp.append(driver.find_element_by_xpath(MRP).text)
            sp.append(driver.find_element_by_xpath(SP).text)

        # print(product_name)

        driver.back()

    except StaleElementReferenceException as Exception:
        pass


# for i in range(6):
#     pp = i + 2
#     url = "https://www.yuvikaherbs.com/categories/herbs?page=" + str(pp)
#     driver.get(url)

#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     elements = len(driver.find_elements_by_xpath("//a[@href]"))

#     for index in range(elements):
#         if(driver.find_elements_by_xpath("//a[@href]")[index].get_attribute("href").find('/products/') != -1):
#             work(driver.find_elements_by_xpath(
#                 "//a[@href]")[index].get_attribute("href"))

# product = {'Name': product_name, 'Weight': weight, 'MRP': mrp, 'SP': sp}
# df = pd.DataFrame(product, columns=['Name', 'Weight', 'MRP', 'SP'])
# print(df)
# df.to_excel(r'Z:\details.xlsx', index=False, header=True)


url = "https://www.yuvikaherbs.com/categories/seeds?page=3"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

elements = len(driver.find_elements_by_xpath("//a[@href]"))
c = 0

for index in range(elements):
    if(driver.find_elements_by_xpath("//a[@href]")[index].get_attribute("href").find('/products/') != -1):
        if(c < 23):
            work(driver.find_elements_by_xpath(
                "//a[@href]")[index].get_attribute("href"))
            c += 1

product = {'Name': product_name, 'Weight': weight, 'MRP': mrp, 'SP': sp}
df = pd.DataFrame(product, columns=['Name', 'Weight', 'MRP', 'SP'])
print(df)
df.to_excel(r'Z:\details.xlsx', index=False, header=True)
