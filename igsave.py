from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


browser=webdriver.Firefox()

browser.get("PUT LINKS HERE FROM INSTAGRAM IMAGE")
classes="FFVAD"
html=browser.page_source
soup=BeautifulSoup(html,"html.parser")
div=soup.find_all("div",{"style","KL4Bh"})
print(div)
images=soup.find("img","FFVAD")
print(images)
string=str(images)
time.sleep(2)

page=images
start_quote = string.find('src="')
end_quote = string.find('" s', start_quote + 1)
url = string[start_quote + 5: end_quote]

url2=url.replace("amp;","")


import requests
import time
timestr = time.strftime("%Y%m%d_%H%M%S")

img_name = "./igsave_{}.jpg".format(timestr)
response = requests.get(url2)
with open(img_name,'wb') as f:
    f.write(response.content)

