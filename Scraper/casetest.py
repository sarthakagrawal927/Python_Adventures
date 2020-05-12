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

url = "https://www.worldometers.info/coronavirus/"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')


countries = []
no_cases = []
no_tests = []
ratio = []

/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[4]/td[1]

for x in range(50):
    name_country = '/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[4]/td[1]'
    cases = '/html/body/div[2]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[' + \
        str(9+x)+']/td[2]'
    tests = '/html/body/div[2]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[' + \
        str(9+x)+']/td[11]'
    countries.append(driver.find_element_by_xpath(name_country).text)
    no_cases.append(driver.find_element_by_xpath(cases).text)
    no_tests.append(driver.find_element_by_xpath(tests).text)

for x in range(50):
    r = int(no_cases[x]) / int(no_tests[x])
    ratio.append(r)

record = {'Country': countries, 'Cases': no_cases,
          'Tests': no_tests, 'Ratio': ratio}
df = pd.DataFrame(record, columns=['Country', 'Cases', 'Tests', 'Ratio'])
print(df)
# df.to_excel(r'Z:\covididetails.xlsx', index=False, header=True)
