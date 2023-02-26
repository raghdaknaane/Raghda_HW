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

# Click on the "Add Movie" logo on the top of website
driver.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()

# Fill in the form to add a new movie
file_input = driver.find_element(By.NAME, "filename")
file_input.send_keys("C:/Users/raghd/OneDrive/Desktop/project2/Tom and Jerry.jpg")

driver.find_element(By.NAME, "movie_title").send_keys("New Movie")
driver.find_element(By.NAME, "director").send_keys("aa")
driver.find_element(By.NAME, "name_actors").send_keys("aaaa,aaa")
driver.find_element(By.NAME, "description").send_keys("aaa")
driver.find_element(By.NAME, "release_year").send_keys("120")
driver.find_element(By.NAME, "video").send_keys("https://www.youtube.com/embed/Rvr68u6k5sI")

# Click the "Add" button to submit the form
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Verify that the new movie appears on the home page
movie_titles = driver.find_elements(By.XPATH, "//div[@class='box']")
lst_movie = []
for movie in movie_titles:
    lst_movie.append(movie.text)
assert 'New Movie' in lst_movie, "FAIL: Movie was not added successfully"
print("Passed: Movie was successfully added")
