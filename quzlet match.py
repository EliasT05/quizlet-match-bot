from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import pandas as pd
import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


# Initialize the Chrome webdriver
options=Options()

fp = FirefoxProfile('C:\\Users\\elias\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ll745f4j.revysys')
options.profile = fp

driver = webdriver.Firefox(options=options)

# Navigate to your Quizlet match game (replace 'quizlet_match_url' with the actual URL)
driver.get('https://quizlet.com/550212425/karbon-kjemi-vg1-flash-cards/?funnelUUID=d2fb309e-1e0c-4ef5-b23b-c3565bf4aded')


# Wait for the page to load
wait = WebDriverWait(driver, 300)
time.sleep(1)

#driver.find_element(By.XPATH,"//button[@aria-label='Start game']").click()

# Find all the terms and definitions on the page
terms = driver.find_elements(By.XPATH, "//span[@class='TermText notranslate lang-en']")
definitions = driver.find_elements(By.XPATH, "//span[@class='SetPageTerm-definitionText']")
'''terms = driver.find_elements(By.CLASS_NAME, "TermText notranslate lang-en")
definitions = driver.find_elements(By.CLASS_NAME, "TermText notranslate lang-no")'''

# Create a dictionary to map terms to definitions
term_dict = {}
for term, definition in zip(terms, definitions):
    term_dict[term.text] = definition.text

#for term, definition in term_dict.items():
    #print(f"{term} :: {definition}")

driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
#driver.get('https://quizlet.com/839376721/match?funnelUUID=7e8e5af6-7aef-43fe-9181-f223d6dd548b')
driver.find_element(By.XPATH, "//a[text()='Match']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Start game']").click()


# Play the game by clicking on each term and its corresponding definition
for term, definition in term_dict.items():
    # Click on the term
    try:
        term_element = driver.find_element(By.XPATH,f"//div[contains(@aria-label, '{term[:8]}')]")
        definition_element = driver.find_element(By.XPATH,f"//div[contains(@aria-label, '{definition[:8]}')]")
        term_element.click()
        definition_element.click()               
        '''
        driver.find_element(By.XPATH,f"//div[contains(@aria-label, '{term[:8]}')]").click()

        # Then click on the corresponding definition
        driver.find_element(By.XPATH,f"//div[contains(@aria-label, '{definition[:8]}')]").click()'''
        pass
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", definition_element)
        driver.execute_script("arguments[0].click();", term_element)
    except Exception as e:
        print( f"{e} term: {term} definition: {definition}")
time.sleep(5)

driver.quit()