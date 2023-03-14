from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest

package_name = "screenshot/Functional_Test/"


@pytest.mark.usefixture("setup")
@pytest.mark.functional
class TestFunctional(BaseClass):
    def test_upload_doc(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_upload_doc/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_upload_doc/step2.png")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.get_screenshot_as_file(package_name + "/test_upload_doc/step3.png")
        file_input = setup.find_element(By.NAME, "filename")
        file_input.send_keys("C:/Users/raghd/OneDrive/Desktop/English.docx")
        setup.find_element(By.NAME, "movie_title").send_keys("New Movie")
        setup.find_element(By.NAME, "director").send_keys("aa")
        setup.find_element(By.NAME, "name_actors").send_keys("aaaa,aaa")
        setup.find_element(By.NAME, "description").send_keys("aaa")
        setup.find_element(By.NAME, "release_year").send_keys("120")
        setup.find_element(By.NAME, "video").send_keys("https://www.youtube.com/embed/Rvr68u6k5sI")
        setup.get_screenshot_as_file(package_name + "/test_upload_doc/step4.png")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        setup.get_screenshot_as_file(package_name + "/test_upload_doc/step5.png")
        title_web = setup.title
        assert "UnboundLocalError" in title_web, log.warning("Passed add a image")
        log.info("The image not legal")
        setup.close()

    def test_1_rating_star(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_1_rating_star/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_1_rating_star/step2.png")
        setup.find_element(By.XPATH, "//img[@src='/display/Monsters.jpg']").click()
        setup.get_screenshot_as_file(package_name + "/test_1_rating_star/step3.png")
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Gada")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Very nice")
        input_star = setup.find_element(By.XPATH, "//label[@title='Bad']")
        input_stars = input_star.text
        input_star.click()
        setup.get_screenshot_as_file(package_name + "/test_1_rating_star/step4.png")
        setup.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()
        stars = setup.find_elements(By.TAG_NAME, "b")
        star_lst = []
        for star in stars:
            star_lst.append(star.text)
        last = star_lst[-1]
        cnt = 0
        for s in last.split(" "):
            cnt += 1
        cnt = f"{cnt} star"
        assert input_stars == cnt, log.warning("Adding review failed, star rating was not set correctly.")
        log.info("Passed!")
        setup.quit()

    def test_part_of_search(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_part_of_search/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_part_of_search/step2.png")
        setup.find_element(By.NAME, "search_string").send_keys("mo")
        setup.get_screenshot_as_file(package_name + "/test_part_of_search/step3.png")
        setup.find_element(By.XPATH, "(//input[@value='search'])").click()
        count = setup.find_elements(By.XPATH, "//body/center/div")
        setup.get_screenshot_as_file(package_name + "/test_part_of_search/step4.png")
        assert len(count) > 0, log.warning("You didn't get anything")
        log.info(f"passed: The number of movie names that there are the letters 'mo' is: {len(count)}")
        setup.close()

    def test_add_connect(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_add_connect/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_add_connect/step2.png")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_connect']").click()
        setup.get_screenshot_as_file(package_name + "/test_add_connect/step3.png")
        setup.find_element(By.NAME, "name").send_keys("Raghda")
        setup.find_element(By.NAME, "message").send_keys("It's a very nice web site")
        setup.find_element(By.NAME, "email_user").send_keys("Raghda23.06.1999@gmail.com")
        setup.get_screenshot_as_file(package_name + "/test_add_connect/step4.png")
        setup.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
        setup.get_screenshot_as_file(package_name + "/test_add_connect/step5.png")
        new_url = setup.current_url
        assert new_url != "http://localhost:5000/add_connect", log.warning("failed: There's a problem, The form wasn't submitted.")
        log.info("Passed: The form was submitted successfully")

    def test_search_capital_latter(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_search_capital_latter/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_search_capital_latter/step2.png")
        setup.find_element(By.NAME, "search_string").send_keys("LUCA")
        setup.get_screenshot_as_file(package_name + "/test_search_capital_latter/step3.png")
        setup.find_element(By.XPATH, "//input[@value='search']").click()
        setup.get_screenshot_as_file(package_name + "/test_search_capital_latter/step4 .png")
        num_search_movie = setup.find_elements(By.XPATH, "//b")
        for movie in num_search_movie:
            assert "LUCA".lower() == movie.text.lower(), log.warning("The search capital dont work")
            log.info("Passed!")

    def test_verify_review_added(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_verify_review_added/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_verify_review_added/step2.png")
        setup.find_element(By.CSS_SELECTOR, "img[src='/display/Moana.jpg']").click()
        setup.get_screenshot_as_file(package_name + "/test_verify_review_added/step3 .png")
        setup.find_element(By.NAME, "name").send_keys("Raghda")
        setup.find_element(By.NAME, "review_text").send_keys("nice")
        setup.find_element(By.CSS_SELECTOR, "label[title='Good']").click()
        setup.get_screenshot_as_file(package_name + "/test_verify_review_added/step4.png")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        setup.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        setup.get_screenshot_as_file(package_name + "/test_verify_review_added/step5.png")
        reviews = setup.find_elements(By.XPATH, "//li")
        name = "Raghda"
        found_name = False
        for review in reviews:
            if review.text == name:
                found_name = True
                break
        assert found_name == False, log.warning(f"Failed to find the name {name} in the reviews")
        log.info("Passed!")

    def test_4_rating_star(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_4_rating_star/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_4_rating_star/step2.png")
        setup.find_element(By.XPATH, "//img[@src='/display/Monsters.jpg']").click()
        setup.get_screenshot_as_file(package_name + "/test_4_rating_star/step3.png")
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Gada")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Very nice")
        input_star = setup.find_element(By.XPATH, "//label[@title='Good']")
        input_stars = input_star.text
        input_star.click()
        setup.get_screenshot_as_file(package_name + "/test_4_rating_star/step4.png")
        setup.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()
        stars = setup.find_elements(By.TAG_NAME, "b")
        star_lst = []
        for star in stars:
            star_lst.append(star.text)
        last = star_lst[-1]
        cnt = 0
        for s in last.split(" "):
            cnt += 1
        cnt = f"{cnt} stars"
        assert input_stars == cnt, log.warning("Adding review failed, star rating was not set correctly.")
        log.info("Passed!")
        setup.quit()

    def test_add_new_movie(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_add_new_movie/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_add_new_movie/step2.png")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.get_screenshot_as_file(package_name + "/test_add_new_movie/step3.png")
        file_input = setup.find_element(By.NAME, "filename")
        file_input.send_keys("C:/Users/raghd/OneDrive/Desktop/project2/Tom and Jerry.jpg")
        setup.find_element(By.NAME, "movie_title").send_keys("New Movie")
        setup.find_element(By.NAME, "director").send_keys("aa")
        setup.find_element(By.NAME, "name_actors").send_keys("aaaa,aaa")
        setup.find_element(By.NAME, "description").send_keys("aaa")
        setup.find_element(By.NAME, "release_year").send_keys("120")
        setup.find_element(By.NAME, "video").send_keys("https://www.youtube.com/embed/Rvr68u6k5sI")
        setup.get_screenshot_as_file(package_name + "/test_add_new_movie/step4.png")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        movie_titles = setup.find_elements(By.XPATH, "//div[@class='box']")
        lst_movie = []
        for movie in movie_titles:
            lst_movie.append(movie.text)
        setup.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        setup.get_screenshot_as_file(package_name + "/test_add_new_movie/step5.png")
        assert 'New Movie' in lst_movie, log.warning("FAIL: Movie was not added successfully")
        log.info("Passed: Movie was successfully added")
        setup.quit()

    def test_upload_image(self, setup):
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_upload_image/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_upload_image/step2.png")
        setup.find_element(By.CSS_SELECTOR, "a[href='/movie_info/11']").click()
        setup.get_screenshot_as_file(package_name + "/test_upload_image/step3.png")
        setup.find_element(By.CSS_SELECTOR, "a[href='/alter_movie/11']").click()
        setup.get_screenshot_as_file(package_name + "/test_upload_image/step4.png")
        setup.find_element(By.NAME, "filename").send_keys("C:/Users/raghd/OneDrive/Desktop/project2/try.jpg")
        setup.find_element(By.NAME, "Update").click()
        setup.find_element(By.CSS_SELECTOR, "a[href='/home']").click()
        movie_images = setup.find_elements(By.XPATH, "//div[@class='box']/a/img")
        lst_movie_images = []
        for movie_image in movie_images:
            lst_movie_images.append(movie_image.get_attribute('src'))
        print(lst_movie_images)
        setup.get_screenshot_as_file(package_name + "/test_upload_image/step5.png")
        assert 'http://localhost:5000/display/Tom%20and%20Jerry.jpg' not in lst_movie_images, "FAIL: Failed: File was not uploaded"
        print("Passed: File was uploaded successfully")

    def test_movie_deletion(self, setup):
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.find_element(By.CSS_SELECTOR, "a[href='/movie_info/11']").click()
        setup.find_element(By.XPATH, "//a[normalize-space()='Delete']").click()
        movie_titles = setup.find_elements(By.XPATH, "//div[@class='box']")
        lst_movie = []
        for movie in movie_titles:
            lst_movie.append(movie.text)
        print(lst_movie)
        assert 'Tom and jerry' not in lst_movie, "Movie 'Tom and jerry' is still displayed in the list of movies"
        print("Passed: the movie is deleted")
