from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


def setup(dev=True):
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    if dev is False:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
