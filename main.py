from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def gmail_link():
    driver.get("https://www.google.com")
    wait = WebDriverWait(driver, 10)
    gmail_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Gmail")))
    assert gmail_link.is_displayed(), "Gmail link is not visible on the page."
    print("Gmail link is present on Google homepage.")


def empik_page_title():
    driver.get("https://www.empik.com/")
    assert "Empik.com" in driver.title
    print("Empik title test passed.")


def empik_foto():
    driver.get("https://www.empik.com/")
    wait = WebDriverWait(driver, 10)
    empik_foto = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='empikfoto.pl']")))
    assert empik_foto.is_displayed(), "Empik foto is not visible on the page."
    print("Empik foto is on the page.")


def empik_bilety():
    driver.get("https://www.empik.com/")
    wait = WebDriverWait(driver, 10)
    empik_bilety = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='empikbilety.pl']")))
    assert empik_bilety.is_displayed(), "Empik bilety is not visible on the page."
    print("Empik bilety is on the page.")


def empik_go():
    driver.get("https://www.empik.com/")
    wait = WebDriverWait(driver, 10)
    empik_go = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='EmpikGO']")))
    assert empik_go.is_displayed(), "Empik go is not visible on the page."
    print("Empik go is on the page.")


def papiernik():
    driver.get("https://www.empik.com/")
    wait = WebDriverWait(driver, 10)
    papiernik = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Papiernik']")))
    assert papiernik.is_displayed(), "Papiernik is not visible on the page."
    print("Papiernik is on the page.")


def shop_page_title():
    driver.get("https://skleptest.pl/")
    assert "Generic Shop" in driver.title
    print("Shop title test passed.")


def shop_username():
    driver.get("https://skleptest.pl/my-account/")
    username = driver.find_element(By.NAME, "username")
    assert username.is_displayed(), "Username input is not visible on the page."
    print("Username input is on the page.")


def shop_password():
    driver.get("https://skleptest.pl/my-account/")
    password = driver.find_element(By.NAME, "password")
    assert password.is_displayed(), "Password input is not visible on the page."
    print("Password input is on the page.")


def shop_register_username():
    driver.get("https://skleptest.pl/my-account/")
    username = driver.find_element(By.NAME, "reg_username")
    assert username.is_displayed(), "Register: username input is not visible on the page."
    print("Register: username input is on the page.")


def shop_register_password():
    driver.get("https://skleptest.pl/my-account/")
    password = driver.find_element(By.NAME, "reg_password")
    assert password.is_displayed(), "Register: password input is not visible on the page."
    print("Register: password input is on the page.")


def shop_login_button():
    driver.get("https://skleptest.pl/my-account/")
    login = driver.find_element(By.NAME, "login")
    assert login.is_displayed(), "Login button input is not visible on the page."
    print("Login button is on the page.")


def shop_register_button():
    driver.get("https://skleptest.pl/my-account/")
    register = driver.find_element(By.NAME, "register")
    assert register.is_displayed(), "Register button input is not visible on the page."
    print("Register button is on the page.")


try:
    dacia_main_page_title()
    dacia_page_title()
    google_main_page_title()
    google_search_button_is_displayed()
    google_search_button_is_displayed()
    google_lucky_search_button_is_displayed()
    google_search()
    gmail_link()
    empik_page_title()
    empik_foto()
    empik_bilety()
    empik_go()
    papiernik()
    shop_page_title()
    shop_username()
    shop_password()
    shop_register_username()
    shop_register_password()
    shop_login_button()
    shop_register_button()
finally:
    driver.quit()
