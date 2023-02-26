# Import required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Open browser in detached mode
service_obj = Service("chromedriver_win32/chromedriver.exe")   # Set the path of the ChromeDriver executable
driver = webdriver.Chrome(service=service_obj, options=chrome_options)    # Create a Chrome browser instance

# Implicit wait for elements to load
driver.implicitly_wait(3)

# Navigate to the website
driver.get("http://localhost:5000/")


# Click on the movie thumbnail to go to the movie information page
driver.find_element(By.CSS_SELECTOR, "img[src='/display/Tom%20and%20Jerry.jpg']").click()

# Click on the 'Alter' button to edit the movie title and poster
driver.find_element(By.CSS_SELECTOR, "a[href='/alter_movie/11']").click()

# Click on the 'Alter' button to edit the movie title and poster
driver.find_element(By.NAME, "filename").send_keys("C:/Users/raghd/OneDrive/Desktop/project2/try.jpg")

# Click the 'Update' button to upload the new movie poster
driver.find_element(By.NAME, "Update").click()

# Click the 'Update' button to upload the new movie poster
driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()

# Click the 'Update' button to upload the new movie poster
movie_images = driver.find_elements(By.XPATH, "//div[@class='box']/a/img")
lst_movie_images = []
for movie_image in movie_images:
    lst_movie_images.append(movie_image.get_attribute('src'))
print(lst_movie_images)

# Check whether the old movie poster URL is not in the list of movie images
assert 'http://localhost:5000/display/Tom%20and%20Jerry.jpg' not in lst_movie_images, "FAIL: Failed: File was not uploaded"
print("Passed: File was uploaded successfully")
