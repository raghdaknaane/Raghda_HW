from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest

package_name = "screenshot/Smoke_Test/"


@pytest.mark.usefixture("setup")
@pytest.mark.smoke
class TestSmoke(BaseClass):

    def test_open_about_us_page(self, setup):
        # Test to check if Add Movie page opens correctly
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_open_about_us_page/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_open_about_us_page/step2.png")
        about_us_link = setup.find_element(By.XPATH, "//img[@src='/static/about.jpg']")
        about_us_link.click()
        setup.get_screenshot_as_file(package_name + "/test_open_about_us_page/step3.png")
        current_url = setup.current_url
        print(current_url)
        assert current_url == "http://localhost:5000/about_us", log.critical("the page not relevance")
        log.info("passed: the page is relevance")
        setup.close()

    def test_open_add_movie(self, setup):
        # Test to check if Add Movie page opens correctly
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_open_add_movie/step2.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_open_add_movie/step2.png")
        add_movie_link = setup.find_element(By.XPATH, "//img[@src='/static/add.png']")
        add_movie_link.click()
        setup.get_screenshot_as_file(package_name + "/test_open_add_movie/step3.png")
        current_url = setup.current_url
        assert current_url == "http://localhost:5000/add_data", log.critical("the page not relevance")
        log.info("passed: the page is relevance")
        setup.close()

    def test_open_connect_us(self, setup):
        # Test to check if Connect Us page opens correctly
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_open_connect_us/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_open_connect_us/step2.png")
        connect_us_link = setup.find_element(By.XPATH, "//img[@src='/static/connect.jpg']")
        connect_us_link.click()
        setup.get_screenshot_as_file(package_name + "/test_open_connect_us/step3.png")
        current_url = setup.current_url
        assert current_url == "http://localhost:5000/add_connect", log.critical("the page not relevance")
        log.info("passed: the page is relevance")
        setup.close()

    def test_open_google_from_icon(self, setup):
        # test to check open google page from icon google
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "/test_open_google_from_icon/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "/test_open_google_from_icon/step2.png")
        setup.find_element(By.CSS_SELECTOR, ".google").click()
        setup.get_screenshot_as_file(package_name + "/test_open_google_from_icon/step3.png")
        assert setup.current_url.startswith("https://www.google.com/search?q=animation+movie&oq=animation+movie&aqs=chrome..69i57j0i512l2j69i59j0i512l2j69i61l2.4894j0j7&sourceid=chrome&ie=UTF-8"), log.critical("FAIL:The Google icon not lead to the correct Google page")
        log.info("Passed!")
        setup.close()

    def test_open_youtube_from_icon(self, setup):
        # test to check open YouTube page from icon YouTube
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.get_screenshot_as_file(package_name + "test_open_youtube_from_icon/step1.png")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        setup.get_screenshot_as_file(package_name + "test_open_youtube_from_icon/step2.png")
        setup.find_element(By.CSS_SELECTOR, ".youtube").click()
        setup.get_screenshot_as_file(package_name + "test_open_youtube_from_icon/step3.png")
        assert setup.current_url.startswith("https://www.youtube.com/results?search_query=animation+movie"), log.critical("FAIL:The Youtube icon not lead to the correct Youtube page")
        log.info("Passed!")
        setup.close()
