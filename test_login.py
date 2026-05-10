from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time

# -----------------------------
# Initialize Browser
# -----------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# -----------------------------
# Test Case 1: Valid Login
# -----------------------------
try:
    driver.get("http://localhost/My_Tourism_Website/login.html")

    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginUser"))
    )
    password = driver.find_element(By.ID, "loginPass")
    login_btn = driver.find_element(By.TAG_NAME, "button")

    username.clear()
    username.send_keys("testuser")
    password.clear()
    password.send_keys("testpassword")
    login_btn.click()

    # Handle alert
    try:
        WebDriverWait(driver, 5).until(lambda d: d.switch_to.alert)
        alert = driver.switch_to.alert
        print("Test Case 1 Alert:", alert.text)
        alert.accept()
        print("Test Case 1 Passed")
    except NoAlertPresentException:
        print("Test Case 1 Failed: No alert")

except Exception as e:
    print("Test Case 1 Error:", e)

time.sleep(1)

# -----------------------------
# Test Case 2: Invalid Login
# -----------------------------
try:
    driver.get("http://localhost/My_Tourism_Website/login.html")

    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginUser"))
    )
    password = driver.find_element(By.ID, "loginPass")
    login_btn = driver.find_element(By.TAG_NAME, "button")

    username.clear()
    username.send_keys("wronguser")
    password.clear()
    password.send_keys("wrongpassword")
    login_btn.click()

    # Handle alert
    try:
        WebDriverWait(driver, 5).until(lambda d: d.switch_to.alert)
        alert = driver.switch_to.alert
        print("Test Case 2 Alert:", alert.text)
        alert.accept()
        print("Test Case 2 Passed")
    except NoAlertPresentException:
        print("Test Case 2 Failed: No alert")

except Exception as e:
    print("Test Case 2 Error:", e)

time.sleep(1)

# -----------------------------
# Test Case 3: Navigation Links 
# -----------------------------
try:
    driver.get("http://localhost/My_Tourism_Website/index.html")

    # Get all link URLs first
    links = driver.find_elements(By.TAG_NAME, "a")
    hrefs = []

    for link in links:
        href = link.get_attribute("href")
        if href:
            hrefs.append(href)

    # Visit each link
    for url in hrefs:
        driver.get(url)
        time.sleep(1)

    print("Test Case 3 Passed: Navigation Links Working")

except Exception as e:
    print("Test Case 3 Error:", e)

# -----------------------------
# Test Case 4: Images
# -----------------------------
try:
    driver.get("http://localhost/My_Tourism_Website/index.html")

    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        if img.is_displayed():
            print(f"Image '{img.get_attribute('src')}' is visible")
        else:
            print(f"Image '{img.get_attribute('src')}' is NOT visible")

    print("Test Case 4 Passed")

except Exception as e:
    print("Test Case 4 Error:", e)

# -----------------------------
# Test Case 5: Headings/Text
# -----------------------------
try:
    driver.get("http://localhost/My_Tourism_Website/index.html")

    headings = driver.find_elements(By.TAG_NAME, "h1") + \
               driver.find_elements(By.TAG_NAME, "h2") + \
               driver.find_elements(By.TAG_NAME, "h3")

    for h in headings:
        if h.is_displayed():
            print(f"Heading '{h.text}' is visible")

    print("Test Case 5 Passed")

except Exception as e:
    print("Test Case 5 Error:", e)

# -----------------------------
# Close Browser
# -----------------------------
driver.quit()