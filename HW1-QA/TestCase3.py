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


# Click on the movie thumbnail to go to the information page
driver.find_element(By.CSS_SELECTOR, "img[src='/display/Tangled.jpg']").click()

# Click the 'Alter' button to edit the movie title
driver.find_element(By.XPATH, "//a[normalize-space()='Alter']").click()

# Enter the new movie title and click the 'Update' button
driver.find_element(By.NAME, "movie_title").send_keys("New name")
driver.find_element(By.NAME, "Update").click()


# Click the Home logo to go back to the homepage
driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()


# Check that the movie title was successfully updated by verifying that the old title is not in the list of movie titles on the homepage
movie_titles = driver.find_elements(By.XPATH, "//div[@class='box']")
lst_movie = []
for movie in movie_titles:
    lst_movie.append(movie.text)
print(lst_movie)
assert 'Tangled' not in lst_movie, "Movie name was not updated"
print("Passed: Movie name was successfully updated to 'New Movie Name")
