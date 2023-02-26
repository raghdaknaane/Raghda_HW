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

# Click on the "About Us" logo
driver.find_element(By.XPATH, "//a[@href='/about_us']").click()


# Check that the current URL is the About Us page and Print a success message if the test passed
assert driver.current_url.startswith("http://localhost:5000/about_us"), "FAIL: The About Us page was not displayed."
print("PASS: The About Us page was displayed.")
