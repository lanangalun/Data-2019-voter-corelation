# import libraries
from bs4 import BeautifulSoup
#import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# specify the url
url = 'https://kawalpemilu.org/#pilpres:42385'

# The path to where you have your chrome webdriver stored:
webdriver_path = 'C:\Users\8.1\Downloads\Programs\chromedriver'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

# Fire up the headless browser
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)

# Load webpage
browser.get(url)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
pretty = soup.prettify()
browser.quit()
# find results within table
results = soup.find('table',{'class':'table'})
rows = results.find_all('tr',{'class':'row'})
list_wilayah = []
jokowi2019 = []
jokowi2014 = []
jumlah = [0,0]
jatim = ['MALANG','PROBOLINGGO','PASURUAN','SIDOARJO','MOJOKERTO','JOMBANG','NGANJUK','MADIUN','NGAWI',
         'KOTA SURABAYA', 'KOTA MADIUN', 'KOTA MOJOKERTO', 'KOTA PASURUAN', 'KOTA PROBOLINGGO','KOTA MALANG']

# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah in jatim:
        satu = data[2].find('span', attrs={'class':'abs'}).getText()

        # Remove decimal point
        satu = satu.replace('.','')

        # Cast Data Type Integer
        satu = int(satu)
        jumlah[0] +=satu
        list_wilayah.append(wilayah)
        jokowi2019.append(satu)

url = 'https://kawalpemilu.org/#pilpres:32676'

# The path to where you have your chrome webdriver stored:
webdriver_path = 'C:\Users\8.1\Downloads\Programs\chromedriver'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

# Fire up the headless browser
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)

# Load webpage
browser.get(url)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
pretty = soup.prettify()
browser.quit()
# find results within table
results = soup.find('table',{'class':'table'})
rows = results.find_all('tr',{'class':'row'})

jateng = ['KARANGANYAR','SRAGEN','PEMALANG','TEGAL','BREBES','KOTA SURAKARTA']

# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah in jateng:
        satu = data[2].find('span', attrs={'class':'abs'}).getText()

        # Remove decimal point
        satu = satu.replace('.','')

        # Cast Data Type Integer
        satu = int(satu)
        jumlah[0] += satu
        list_wilayah.append(wilayah)
        jokowi2019.append(satu)

url = 'https://2014.kawalpemilu.org/#0.42385'

# The path to where you have your chrome webdriver stored:
webdriver_path = 'C:\Users\8.1\Downloads\Programs\chromedriver'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

# Fire up the headless browser
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)

# Load webpage
browser.get(url)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
pretty = soup.prettify()
browser.quit()
# find results within table
results = soup.find('table',{'class':'aggregate'})
rows = results.find_all('tr',{'class':'datarow'})

jatimb = ['KOTA SURABAYA', 'KOTA MADIUN', 'KOTA MOJOKERTO', 'KOTA PASURUAN', 'KOTA PROBOLINGGO','KOTA MALANG',
          'MALANG','PROBOLINGGO','PASURUAN','SIDOARJO','MOJOKERTO','JOMBANG','NGANJUK','MADIUN','NGAWI']
# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')

    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah in jatimb:

        dua = data[10].getText()
        # Remove decimal point

        dua = dua.replace('.', '')
        # Cast Data Type Integer


        dua = int(dua)
        jumlah[1] += dua
        jokowi2014.append(dua)

url = 'https://2014.kawalpemilu.org/#0.32676'

# The path to where you have your chrome webdriver stored:
webdriver_path = 'C:\Users\8.1\Downloads\Programs\chromedriver'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

# Fire up the headless browser
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)

# Load webpage
browser.get(url)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
pretty = soup.prettify()
browser.quit()
# find results within table
results = soup.find('table',{'class':'aggregate'})
rows = results.find_all('tr',{'class':'datarow'})

for r in rows:
    # find all columns per result
    data = r.find_all('td')

    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah in jateng:

        dua = data[10].getText()
        # Remove decimal point

        dua = dua.replace('.', '')
        # Cast Data Type Integer


        dua = int(dua)
        jumlah[1] += dua
        jokowi2014.append(dua)

print jumlah
# Convert to numpy
np_wilayah = np.array(list_wilayah)
np_jokowi2019= np.array(jokowi2019)
np_jokowi2014= np.array(jokowi2014)
print np_wilayah

# plot data
fig,ax = plt.subplots(figsize=(10,5))
# fig,ax = plt.subplots()
# print(ax)
pos = list(range(len(np_jokowi2014)))
width = 0.25

# print(ind-width/2)

rects1 = ax.bar(pos,np_jokowi2014,width,color='red',label='Jokowi 2014')
rects2 = ax.bar([p + width for p in pos],np_jokowi2019,width,color='blue',label='Jokowi 2019')
# ax.set_xticks(ind)
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(np_wilayah)
# # Naming label
plt.xlabel('wilayah')
plt.ylabel('perolehan suara')
# Set Text Value
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
# # styling x,y value
# plt.xticks(rotation=30,ha='right')
plt.yticks(np.arange(np_jokowi2019.min(),np_jokowi2014.max(),4000000))
plt.xticks(rotation=30,ha='right')
plt.legend(loc='upper right')
plt.yscale('linear')


plt.show()