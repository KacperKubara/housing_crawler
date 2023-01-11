from selenium.webdriver.common.by import By
import yagmail

import time 
import re


class OurDomainCrawler():
    def __init__(self, driver):
        self.driver = driver
        self.result_dict = {}
        self.URL_BASE = "https://southeast-thisisourdomain.securerc.co.uk/onlineleasing/ourdomain-amsterdam-south-east/floorplans.aspx?"
        self.yag = yagmail.SMTP('shukakaciupaga1', 'xqumputsinsfharm')
        
    def run(self):
        self.driver.get(self.URL_BASE)
        time.sleep(1)
        element = self.driver.find_element('id', 'divFPRows')
        data_arr = element.find_elements(By.TAG_NAME, 'tr')

        print("Iterate over rows")
        for i in range(len(data_arr)):
            prop_name = data_arr[i].find_element(By.XPATH, f"//td[@data-label='Floor Plan'][@data-selenium-id='FPlan_{str(i+1)}']")
            availability = data_arr[i].find_element(By.XPATH, f"//td[@data-label='Availability'][@data-selenium-id='Availability_{str(i+1)}']")
            data_dict = self.parse_data({
                "prop_name": prop_name.get_attribute('outerHTML'), 
                "availability": availability.get_attribute('outerHTML')
                })
            if "notified" not in data_dict["avail_str"].lower():
                self.result_dict[data_dict["prop_name"]] = data_dict["avail_str"]
            print(data_dict)
        
        self.result_dict = {"chuj": "test"}
        if self.result_dict:
            print("Sending email")
            self.send_email_to_me(self.result_dict)

    def parse_data(self, data_el):
        prop = data_el["prop_name"]
        avail = data_el["availability"]
        
        prop_str = re.search('title="(.*)"', prop).group(1)
        avail_str = re.search('([a-zA-Z ]+)<\/button><\/td>', avail).groups()[-1]
        return {
            "prop_name": prop_str,
            "avail_str": avail_str
            }

    def send_email_to_me(self, result_dict):
        body_text = f"Hi mate, go to URL: {self.URL_BASE} \n\n There seems to be something there: {str(result_dict)}"
        self.yag.send('kacper.kubara.ai@gmail.com', 'Housing notification', body_text)
