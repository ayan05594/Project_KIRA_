from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--headless")  


driver = webdriver.Chrome(service=service, options=options)
driver.get("https://kiit.ac.in/")


time.sleep(3)


page_text = driver.find_element(By.TAG_NAME, "body").text


with open("kiit_homepage.txt", "w", encoding="utf-8") as f:
    f.write(page_text)


driver.quit()

print("✅ Data saved to kiit_homepage.txt")