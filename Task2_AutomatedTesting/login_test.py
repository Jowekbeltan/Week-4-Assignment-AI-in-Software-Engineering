from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/login")

driver.find_element(By.ID, "username").send_keys("user1")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "login-btn").click()

assert "dashboard" in driver.current_url
driver.quit()
