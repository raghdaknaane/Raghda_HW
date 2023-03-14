import time
import imageio
from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest

# package_name = "screenshot/Smoke_Test/" + __name__


@pytest.mark.usefixture("setup")
@pytest.mark.smoke
class TestSmoke(BaseClass):

    def test_open_about_us_page(self, setup):
        # test to check open about us page
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://localhost:5000/")
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("raghda@gmail.com")
        setup.find_element(By.XPATH, "//input[@type='password']").send_keys("Raghda")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        about_us_link = setup.find_element(By.XPATH, "//img[@src='/static/about.jpg']")
        about_us_link.click()
        time.sleep(1)
        current_url = setup.current_url
        assert current_url == "http://localhost:5000/about_us", log.critical("the page not relevance")
        log.info("passed: the page is relevance")
        # Take screenshots and save to a list
        screenshots = []
        screenshots.append(imageio.imread(setup.get_screenshot_as_png(), format='png'))
        time.sleep(1)
        about_us_link.click()
        screenshots.append(imageio.imread(setup.get_screenshot_as_png(), format='png'))
        # Save screenshots as GIF
        imageio.mimsave('about_us.gif', screenshots, fps=2)

    # ... the rest of the code is the same
