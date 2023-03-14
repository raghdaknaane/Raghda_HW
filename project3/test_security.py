from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest

package_name = "screenshot/Security_Test/"


@pytest.mark.usefixture("setup")
@pytest.mark.security
class TestSecurity(BaseClass):
    def test_uploading_gif_image(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_uploading_gif_image/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_uploading_gif_image/step2.png")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.get_screenshot_as_file(package_name + "/test_uploading_gif_image/step3.png")
        file_input = setup.find_element(By.NAME, "filename")
        file_input.send_keys("C:/Users/raghd/OneDrive/Desktop/project2/gif.gif")
        setup.find_element(By.NAME, "movie_title").send_keys("Movie")
        setup.find_element(By.NAME, "director").send_keys("aa")
        setup.find_element(By.NAME, "name_actors").send_keys("aaaa,aaa")
        setup.find_element(By.NAME, "description").send_keys("aaa")
        setup.find_element(By.NAME, "release_year").send_keys("120")
        setup.find_element(By.NAME, "video").send_keys("https://www.youtube.com/embed/Rvr68u6k5sI")
        setup.get_screenshot_as_file(package_name + "/test_uploading_gif_image/step4.png")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        setup.get_screenshot_as_file(package_name + "/test_uploading_gif_image/step5.png")
        title_web = setup.title
        assert "UnboundLocalError" in title_web, log.warning("FAIL: Movie was  added successfully")
        log.info("Passed: Movie wasn't successfully added")
        setup.close()

    def test_existing_username_password(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("Raghda_knaane@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_existing_username_password/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        title_web = setup.title
        setup.get_screenshot_as_file(package_name + "/test_existing_username_password/step2.png")
        assert "Animation Movies" in title_web, log.warning("FAIL")
        log.info("Passed")
        setup.close()

    def test_correct_username_incorrect_password(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("Raghda_knaane@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("12345")
        setup.get_screenshot_as_file(package_name + "/test_correct_username_incorrect_password/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        wrong_message = setup.find_element(By.XPATH, "//h3[normalize-space()='Wrong username or password']")
        setup.get_screenshot_as_file(package_name + "/test_correct_username_incorrect_password/step2.png")
        assert wrong_message.is_displayed(), log.warning("FAIL")
        log.info("Passed")
        setup.close()

    def test_not_existing_username_password(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("stam@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("stam1234")
        setup.get_screenshot_as_file(package_name + "/test_not_existing_username_password/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        wrong_message = setup.find_element(By.XPATH, "//h3[normalize-space()='Wrong username or password']")
        setup.get_screenshot_as_file(package_name + "/test_not_existing_username_password/step2.png")
        assert wrong_message.is_displayed(), log.warning("FAIL")
        log.info("Passed")
        setup.close()

    def test_incorrect_username_existing_password(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("stam123@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_incorrect_username_existing_password/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        wrong_message = setup.find_element(By.XPATH, "//h3[normalize-space()='Wrong username or password']")
        setup.get_screenshot_as_file(package_name + "/test_incorrect_username_existing_password/step2.png")
        assert wrong_message.is_displayed(), log.warning("FAIL")
        log.info("Passed")
        setup.close()

    def test_incorrect_username_not_existing_password(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("stam123@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("knaane123")
        setup.get_screenshot_as_file(package_name + "/test_incorrect_username_not_existing_password/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        wrong_message = setup.find_element(By.XPATH, "//h3[normalize-space()='Wrong username or password']")
        setup.get_screenshot_as_file(package_name + "/test_incorrect_username_not_existing_password/step2.png")
        assert wrong_message.is_displayed(), log.warning("FAIL")
        log.info("Passed")
        setup.close()
