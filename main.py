from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def dacia_main_page_title():
    driver.get("https://www.dacia.pl/")
    assert "DACIA" in driver.title
    print("Dacia title test passed.")


def dacia_page_title():
    driver.get("https://umowjazde.dacia.pl/")
    assert "Jazda" in driver.title
    print("Dacia umowjazde title test passed.")


def google_main_page_title():
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print("Google title test passed.")


def google_search_button_is_displayed():
    driver.get("https://www.google.com")
    search_button = driver.find_element(By.NAME, "btnK")
    assert search_button.is_displayed()
    print('"Search" button test passed.')


def google_lucky_search_button_is_displayed():
    driver.get("https://www.google.com")
    lucky_button = driver.find_element(By.NAME, "btnI")
    assert lucky_button.is_displayed()
    print('"I\'m Feeling Lucky" button test passed.')


def google_search():
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0
    print("Search results test passed.")


try:
    dacia_main_page_title()
    dacia_page_title()
    google_main_page_title()
    google_search_button_is_displayed()
    google_search_button_is_displayed()
    google_lucky_search_button_is_displayed()
    google_search()
finally:
    driver.quit()
