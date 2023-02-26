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

# Click the "Connect Us" logo
driver.find_element(By.CSS_SELECTOR, "a[href='/add_connect']").click()

# Fill in the form fields (name, message, and email)
driver.find_element(By.NAME, "name").send_keys("Raghda")
driver.find_element(By.NAME, "message").send_keys("It's a very nice web site")
driver.find_element(By.NAME, "email_user").send_keys("Raghda23.06.1999@gmail.com")

# Submit the form
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

# Verify that the user is redirected to the home page
new_url = driver.current_url
assert new_url != "http://localhost:5000/add_connect", "failed: There's a problem, The form wasn't submitted."
print("Passed: The form was submitted successfully")
