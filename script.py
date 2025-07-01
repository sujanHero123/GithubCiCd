from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure Chrome options for headless CI run
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Needed for CI
options.add_argument("--disable-dev-shm-usage")  # Prevent crashes in CI

# Setup WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Google and perform a search
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("GitHub Actions with Selenium and WebDriverManager")
search_box.send_keys(Keys.RETURN)

time.sleep(2)
print("Title:", driver.title)

driver.quit()
