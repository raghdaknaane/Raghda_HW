import time
from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest

package_name = "screenshot/Acceptance_Test/"


@pytest.mark.usefixture("setup")
@pytest.mark.acceptance
class TestAcceptance(BaseClass):

    def test_video_displayed(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_video_displayed/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_video_displayed/step2.png")
        setup.find_element(By.XPATH, "//img[@src='/display/Tangled.jpg']").click()
        setup.get_screenshot_as_file(package_name + "/test_video_displayed/step3.png")
        setup.find_element(By.CSS_SELECTOR, "iframe[width='500']").click()
        setup.get_screenshot_as_file(package_name + "/test_video_displayed/step4.png")
        assert setup.find_element(By.CSS_SELECTOR, "iframe[width='500']").is_displayed(), log.warning("FAIL: Video is not displayed")
        log.info("PASS: Video is displayed")
        setup.close()

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

    def test_alter_name_of_movie(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_alter_name_of_movie/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_alter_name_of_movie/step2.png")
        setup.find_element(By.CSS_SELECTOR, "img[src='/display/Tangled.jpg']").click()
        setup.get_screenshot_as_file(package_name + "/test_alter_name_of_movie/step3.png")
        setup.find_element(By.XPATH, "//a[normalize-space()='Alter']").click()
        setup.find_element(By.NAME, "movie_title").send_keys("Tangled New")
        setup.get_screenshot_as_file(package_name + "/test_alter_name_of_movie/step4.png")
        setup.find_element(By.NAME, "Update").click()
        setup.find_element(By.CSS_SELECTOR, "a[href='/home']").click()
        movie_titles = setup.find_elements(By.XPATH, "//div[@class='box']")
        lst_movie = []
        for movie in movie_titles:
            lst_movie.append(movie.text)
        setup.get_screenshot_as_file(package_name + "/test_alter_name_of_movie/step5.png")
        assert 'Tangled' not in lst_movie, log.warning("Movie name was not updated")
        log.info("Passed: Movie name was successfully updated to 'New Movie Name")
        setup.quit()

    def test_scroll_to_top(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_scroll_to_top/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_scroll_to_top/step2.png")
        button_up = setup.find_element(By.XPATH, "//a[@class='top']")
        setup.execute_script("window.scrollTo(100, 100);")
        time.sleep(4)
        setup.get_screenshot_as_file(package_name + "/test_scroll_to_top/step3.png")
        button_up.click()
        setup.execute_script("window.scrollTo(0, 0);")
        scroll_position = setup.execute_script("return window.pageYOffset;")
        setup.get_screenshot_as_file(package_name + "/test_scroll_to_top/step4.png")
        assert scroll_position == 0, log.warning("failed: The button don't work")
        log.info("Passed: The button worked")

    def test_home_logo(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_home_logo/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_home_logo/step2.png")
        setup.find_element(By.XPATH, "//img[@src='/display/Tangled.jpg']").click()
        setup.get_screenshot_as_file(package_name + "/test_home_logo/step3.png")
        setup.find_element(By.CSS_SELECTOR, "a[href='/home']").click()
        setup.get_screenshot_as_file(package_name + "/test_home_logo/step4.png")
        assert setup.current_url == "http://localhost:5000/home", log.warning(
            "FAIL: Clicking on Home logo did not take user back to home page")
        log.info("PASS: Clicking on Home logo took user back to home page")
        setup.close()
