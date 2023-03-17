#IMPORTS

import requests
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datefinder
from selenium.webdriver.chrome.options import Options
from lxml import etree
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path # 
import csvwriter
import csv
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions

userAgent=["Mozilla/5.0 (Windows NT 10.0; Win64; x64)","AppleWebKit/537.36 (KHTML, like Gecko)","Chrome/84.0.4147.56 Safari/537.36"]





#OPTIONS FOR SELENIUM , headless = true means it wont open browser, detach = true means it wont close if opened
options=FirefoxOptions()
options.add_argument(f'user-agent={userAgent}')
options.headless=False
options.add_argument("--disable-gpu")
options.add_argument("--window-size=960,1080")
#options.add_experimental_option('detach',True)
options.add_argument("--ignore-certificate-errors")
options.add_argument('--allow-running-insecure-content')
#options.add_experimental_option('excludeSwitches', ['enable-logging'])

caps = webdriver.DesiredCapabilities.FIREFOX.copy()
caps['acceptInsecureCerts'] = True
options.add_argument('--disable-dev-shm-usage')
caps['acceptInsecureCerts'] = True

driver = webdriver.Firefox(options=options)




#KEYWORDS = FOTIA,RIPANSI,KOSMOS,KUKLOFORIA,TROXAIO,DROMOS,ERGA,AGONES,PROMI8EAS

all_best_urls=['https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CF%80%CE%BB%CE%AE%CE%B8%CE%BF%CF%82','https://www.thebest.gr/feed/search/?q=%CF%80%CF%85%CF%81%CE%BA%CE%B1%CE%B3%CE%B9%CE%AC%20%CF%80%CE%AC%CF%84%CF%81%CE%B1',
'https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CF%84%CF%81%CE%BF%CF%87%CE%B1%CE%AF%CE%BF',
'https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CE%B3%CE%AE%CF%80%CE%B5%CE%B4%CE%BF',
'https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CF%80%CF%81%CE%BF%CE%BC%CE%B7%CE%B8%CE%AD%CE%B1%CF%82',
'https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CE%B1%CE%B3%CF%8E%CE%BD%CE%B1%CF%82',
'https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CE%B1%CF%84%CE%BC%CF%8C%CF%83%CF%86%CE%B1%CE%B9%CF%81%CE%B1',
'https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CF%80%CE%BF%CF%81%CE%B5%CE%AF%CE%B1',
'https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CF%81%CF%8D%CF%80%CE%B1%CE%BD%CF%83%CE%B7',
'https://www.thebest.gr/feed/search/?q=%CE%BA%CF%85%CE%BA%CE%BB%CE%BF%CF%86%CE%BF%CF%81%CE%AF%CE%B1%20%CF%80%CE%AC%CF%84%CF%81%CE%B1','https://www.thebest.gr/feed/search/?q=%CF%80%CE%AC%CF%84%CF%81%CE%B1%20%CE%BC%CE%B9%CE%BA%CF%81%CE%BF%CF%83%CF%89%CE%BC%CE%B1%CF%84%CE%AF%CE%B4%CE%B9%CE%B1']


#21/1/2023 19:00
basic_url=all_best_urls[10]

#START OF CRAWL AND AUTOMATION
'''


driver.get(basic_url)
time.sleep(10)
innerHTML=driver.execute_script('return document.body.innerHTML')

soup=BeautifulSoup(innerHTML,features='lxml')
time.sleep(5)



element=driver.find_element(By.CLASS_NAME,value='css-1cqq2gu')
if (element is not None):
    element.click()
    
#FIRST TIME

links=[]
urls=soup.find_all('a',class_='gs-title' ,href=True)
for url in urls:
    links.append(url['href'])

print(len(links))
links2=[*set(links)]
print(len(links2))

innerHTML2=driver.execute_script('return document.body.innerHTML')
soup=BeautifulSoup(innerHTML2,features='lxml')


for i in range(len(links2)):
            url=links2[i]
            driver.get(url)
            time.sleep(3)
            innerHTML=driver.execute_script('return document.body.innerHTML')
            
            soup2=BeautifulSoup(innerHTML,features='lxml')
            title=soup2.find('h1',class_='m-0 font-condensed font-weight-bold font-grey article-header')
            content=soup2.find('div',class_='bodypart-text')
            date=soup2.find('time')
            if (title):
                with open("input.csv", "a+", encoding='utf-8',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([title.text,date['datetime'],content.text])
                    csvfile.close()
print('finished first page and now will scroll')    

'''
#SECOND UNTIL LAST PAGE

for j in range(8,9):
    
    driver.get(basic_url)
    time.sleep(10)
    try:
        element=driver.find_element(By.CLASS_NAME,value='css-1cqq2gu').click()
    except:
        pass
    
    driver.execute_script("window.scrollTo(0, 2200);")
    
    driver.find_element(By.XPATH,f'''//*[@id="___gcse_2"]/div/div/div/div[5]/div[2]/div[1]/div/div[2]/div/div[{j}]''').click()


    time.sleep(10)
    innerHTML3=driver.execute_script('return document.body.innerHTML')
    soup=BeautifulSoup(innerHTML3,features='lxml')


    links=[]
    time.sleep(5)
    urls=soup.find_all('a',class_='gs-title' ,href=True)
    for url in urls:
        links.append(url['href'])

    print(len(links))
    links2=[*set(links)]
    print(len(links2))
    innerHTML2=driver.execute_script('return document.body.innerHTML')
    soup=BeautifulSoup(innerHTML2,features='lxml')

    
    for i in range(len(links2)):
            url=links2[i]
            driver.get(url)
            time.sleep(5)
            innerHTML=driver.execute_script('return document.body.innerHTML')
            soup2=BeautifulSoup(innerHTML,features='lxml')
            title=soup2.find('h1',class_='m-0 font-condensed font-weight-bold font-grey article-header')
            content=soup2.find('div',class_='bodypart-text')
            date=soup2.find('time')
            if (title is not None):
                with open("input.csv", "a+", encoding='utf-8',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    print(title.text)
                    writer.writerow([title.text,date['datetime'],content.text])
                    csvfile.close()
    time.sleep(5)
