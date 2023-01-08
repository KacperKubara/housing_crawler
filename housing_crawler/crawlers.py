import time 
from selenium.webdriver.common.by import By
import re


class OurDomainCrawler():
    def __init__(self, driver):
        self.driver = driver
        
        self.URL_BASE = "https://southeast-thisisourdomain.securerc.co.uk/onlineleasing/ourdomain-amsterdam-south-east/floorplans.aspx?"

    
    def run(self):
        self.driver.get(self.URL_BASE)
        time.sleep(1)
        element = self.driver.find_element('id', 'divFPRows')
        data_arr = element.find_elements(By.TAG_NAME, 'tr')
        
        print("Iterate over rows")
        for i in range(len(data_arr)):
            prop_name = data_arr[i].find_element(By.XPATH, "//td[@data-label='Floor Plan']")
            availability = data_arr[i].find_element(By.XPATH, "//td[@data-label='Availability']")

            data_dict = self.parse_data({
                "prop_name": prop_name.get_attribute('outerHTML'), 
                "availability": availability.get_attribute('outerHTML')
                })
            print(data_dict)
    
    def parse_data(self, data_el):
        prop = data_el["prop_name"]
        avail = data_el["availability"]
        
        prop_str = re.search('title="(.*)"', prop).group(1)
        avail_str = re.search('([a-zA-Z ]+)<\/button><\/td>', avail).groups()[-1]
        return {
            "prop_name": prop_str,
            "avail_str": avail_str
            }
