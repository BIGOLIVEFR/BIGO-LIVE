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
