# Import required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# Implicit wait for elements to load
driver.implicitly_wait(3)

# Navigate to the website
driver.get("http://localhost:5000/")

# Click on the movie Tangled
driver.find_element(By.XPATH, "//img[@src='/display/Tangled.jpg']").click()

# Click on the trailer link
driver.find_element(By.CSS_SELECTOR, "iframe[width='500']").click()

# Verify that the video is playing and Print a success message if the test passed
assert driver.find_element(By.CSS_SELECTOR, "iframe[width='500']").is_displayed(), "FAIL: Video is not displayed"
print("PASS: Video is displayed")
