from bs4 import BeautifulSoup
import requests

import urllib
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options,
                          executable_path="C:\Chrome Driver\chromedriver.exe")


def downloadInstagramPosts(profile):
    link = "https://www.instagram.com/" + profile + "/"
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    if soup.find("h2", {"class": "rkEop"}) != "None" and soup.find("h2", {"class": "rkEop"}) == "This Account is Private":
        print("This account is private.")
    else:
        images = soup.find_all("img", {"class": "FFVAD"})
        name = soup.find("h1", {"class": "rhpdm"}).getText()
        os.makedirs(name)
        currentDirectory = os.getcwd()
        newDirectory = os.path.join(currentDirectory, './'+name)
        for x in range(0, len(images)):
            imageFileName = "Image"+str(x)+".jpg"
            imageFileDirectory = os.path.join(newDirectory, imageFileName)
            urllib.request.urlretrieve(images[x].get(
                "src"), imageFileDirectory)


profile = input("Username: @")
downloadInstagramPosts(profile)
