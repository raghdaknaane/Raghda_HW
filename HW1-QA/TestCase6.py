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


# Click on the movie poster to go to its detail page (I want to delete a tom and Jerry).
driver.find_element(By.CSS_SELECTOR, "img[src='/display/Tom%20and%20Jerry.jfif']").click()


# Click on the "Delete" button.
driver.find_element(By.XPATH, "//a[normalize-space()='Delete']").click()

# Get and print the titles of all the movies on the page
movie_titles = driver.find_elements(By.XPATH, "//div[@class='box']")
lst_movie = []
for movie in movie_titles:
    lst_movie.append(movie.text)
print(lst_movie)

# Verify that the movie is no longer displayed in the list of movies and Print a success message if the test passed
assert 'Tom and jerry' not in lst_movie, "Movie 'Tom and jerry' is still displayed in the list of movies"
print("Passed: the movie is deleted")
