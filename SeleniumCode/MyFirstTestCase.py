# 1.Open browser(chrome/edge)
# 2.With this link https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 3.Give creds, Login and check title before and after login
import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service -> driver loc
from selenium.webdriver.common.by import By
# import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

# servicess = Service("D:\Selenium\Drivers\chromedriver.exe") driver loc

# driver = webdriver.Chrome(service=servicess) driver loc
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(1.0)
# time.sleep(5)
username = driver.find_element(By.XPATH, '//input[@name="username"]').is_displayed()
print(username)
# if not username:
#     driver.implicitly_wait(1.0)
#     print(username, "after delay")

driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
driver.find_element(By.XPATH, '//button[text()=" Login "]').click()

Act_Title = driver.title
Exp_Title = "OrangeHRM"

if Act_Title == Exp_Title:
    print("Login test passed")
else:
    print("Login failed")

# driver.close()



