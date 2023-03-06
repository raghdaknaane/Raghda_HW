from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("../chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("Raghda")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Raghda23.06.1999@gmail.com")
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("Raghda1-")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()
driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']/option[text()='Female']").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()




driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("23/6/1999")
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
successText = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success!" in successText, "Test failed"
print("Test passed")


