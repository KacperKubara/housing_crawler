from crawlers import OurDomainCrawler

from selenium_setup import setup


if __name__ == "__main__":
    print("Crawler Setup")
    driver = setup(dev=False)
    
    print("Initiate and run the crawler...")
    crawler = OurDomainCrawler(driver=driver)
    crawler.run()
