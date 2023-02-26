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

# Enter search string and click the search button
driver.find_element(By.NAME, "search_string").send_keys("mo")
driver.find_element(By.XPATH, "(//input[@value='search'])").click()

# Assert that the list has a length greater than 0, meaning search results were returned
# and Print the number of search results found with relevant message

count = driver.find_elements(By.XPATH, "//body/center/div")
assert len(count) > 0, "You didn't get anything"
print(f"passed: The number of movie names that there are the letters 'mo' is: {len(count)}")
