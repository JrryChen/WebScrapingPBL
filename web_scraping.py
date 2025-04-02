from sys import executable

from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # to allow search by parameters
from selenium.webdriver.support.ui import WebDriverWait # to wait for the webpage to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the webpage has been loaded
from selenium.common.exceptions import TimeoutException # TO handle timeout situation

#Code to open new browser window
driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = "C:/Users/chess/PycharmProjects/WebScrapingPBL/chromedriver-win64/chromedriver-win64/chromedriver.exe"

def create_webdriver():
 return webdriver.Chrome()

if __name__ == "__main__":
    browser = create_webdriver()
    browser.get("https://github.com/collections/machine-learning")
    # "//" finds all h1 elements, [@class=...] selects the ones with the attribute class = 'h3...'
    projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

    project_list = {}
    for project in projects:
        proj_name = project.text
        # ./ finds <a> elements under the project node, [0] gets the first <a> element, .get_attribute gets the attribute value
        proj_url = project.find_elements(By.XPATH, "./a")[0].get_attribute("href")
        project_list[proj_name] = proj_url

    print(project_list)