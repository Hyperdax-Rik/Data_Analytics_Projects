from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=31O7TOIT00HGT&sprefix=lapt%2Caps%2C403&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elems)
    # print(elem.get_attribute("outerHTML"))
    time.sleep(2)

    driver.close()