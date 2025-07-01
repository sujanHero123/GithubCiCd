from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options for headless execution (good for CI)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate directly to Wikipedia's Nepal page
driver.get("https://en.wikipedia.org/wiki/Nepal")

# Wait for the page to fully load
time.sleep(2)

# Extract the 8th paragraph in the content
try:
    element = driver.find_element(By.CSS_SELECTOR, "#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(8)")
    print("Extracted Paragraph:\n", element.text)
except Exception as e:
    print("Failed to extract paragraph:", e)

driver.quit()
