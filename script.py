from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver (make sure chromedriver is in PATH or provide path manually)
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.google.com")

# Find the search box by name and enter a search query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)  # Press Enter

# Wait for results to load (basic sleep, or use WebDriverWait for dynamic wait)
time.sleep(2)

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
