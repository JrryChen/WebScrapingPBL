from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # to allow search by parameters
from selenium.webdriver.support.ui import WebDriverWait # to wait for the webpage to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the webpage has been loaded
from selenium.common.exceptions import TimeoutException # TO handle timeout situation

#Code to open new browser window
webdriver = webdriver.ChromeOptions()
webdriver.option.add_argument("--incognito")
webdriver_path = "C:/Users/chess/PycharmProjects/WebScrapingPBL/"