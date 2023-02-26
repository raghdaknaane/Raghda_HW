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

# Click on the Google icon
driver.find_element(By.CSS_SELECTOR, ".google").click()

# Verify that the correct Google page has loaded and Print a success message if the test passed
assert driver.current_url.startswith("https://www.google.com/search?q=animation+movie&oq=animation+movie&aqs=chrome..69i57j0i512l2j69i59j0i512l2j69i61l2.4894j0j7&sourceid=chrome&ie=UTF-8"), "FAIL:The Google icon not lead to the correct Google page"
print("Passed!")
