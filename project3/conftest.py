from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import inspect
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture(params=["chrome", "edge"])
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    if request.param == "chrome":
        service_obj = Service("chromedriver_win32/chromedriver")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        driver = None

    driver.implicitly_wait(8)
    driver.maximize_window()

    yield driver

    if driver:
        driver.quit()
