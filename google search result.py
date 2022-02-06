from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")


def google_search():
    search_google = driver.find_element(By.NAME, 'q')
    search_google.send_keys("Github Tutorial")