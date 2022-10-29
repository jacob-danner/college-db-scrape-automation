from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

def download_zips(num_quarterly_periods):
    cwd = os.getcwd()
    try:
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': cwd}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
        driver.get('https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx')

        type_selection = driver.find_element(By.XPATH, '//*[@id="ListBox1"]/option[1]')
        type_selection.click() # Call Reports -- single period

        # iterate throught the selctions dropdown
        for i in range(num_quarterly_periods): 
                period_selector = Select( driver.find_element(By.XPATH, '//*[@id="DatesDropDownList"]') )
                period = period_selector.select_by_index(i) 

                download_button = driver.find_element(By.XPATH, '//*[@id="Download_0"]')
                download_button.click()

                time.sleep(2)

        time.sleep(10)
        driver.close()

    except:
        raise Exception('issue scraping data')