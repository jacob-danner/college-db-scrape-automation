from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

def download_zip():
    cwd = os.getcwd()
    try:
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': cwd}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
        driver.get('https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx')

        type_selection = driver.find_element(By.XPATH, '//*[@id="ListBox1"]/option[1]')
        type_selection.click() # Call Reports -- single period

        period_selector = Select( driver.find_element(By.XPATH, '//*[@id="DatesDropDownList"]') )
        periods_options = period_selector.options # returns a list of WebElements. 
        period = period_selector.select_by_index(0) # first option in selector

        download_button = driver.find_element(By.XPATH, '//*[@id="Download_0"]')
        download_button.click()

        time.sleep(5)
        driver.close()

    except:
        raise Exception('issue scraping data')
    