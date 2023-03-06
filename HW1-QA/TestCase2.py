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

# Click on the tangled movie image
driver.find_element(By.XPATH, "//img[@src='/display/Tangled.jpg']").click()


# Click on the Home logo to go back to the home page
driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()

# Check if the current URL is the home page and Print a success message if the code reaches this point
assert driver.current_url == "http://localhost:5000/", "FAIL: Clicking on Home logo did not take user back to home page"
print("PASS: Clicking on Home logo took user back to home page")
