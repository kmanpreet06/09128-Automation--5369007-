from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com/")


def youtube_search():
    search_youtube = driver.find_element(By.NAME, 'search_query')
    search_youtube.send_keys("Tutorial of Github")
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs