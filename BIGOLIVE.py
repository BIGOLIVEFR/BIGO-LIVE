from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://www.bigo.tv/petitlion18')

# Find the element using XPath and click it
element = driver.find_element(By.XPATH, "//*[contains(@class, 'host-follow-btn')]")
element.click()

# Close the browser
driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the element to be present and clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'host-follow-btn')]"))
)
element.click()
