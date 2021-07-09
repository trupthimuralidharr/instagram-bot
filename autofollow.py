from selenium import webdriver
from time import sleep
#driver=webdriver.Chrome()
driver=webdriver.Chrome(executable_path=r"C:\Users\trupt\OneDrive\Desktop\practice\MadLib\chromedriver.exe")
driver.get("https://www.instagram.com")
sleep(4)
driver.find_element_by_xpath(("//input[@name=\"username\"]")).send_keys(("jasmin.jupiter.jam22"))
driver.find_element_by_xpath(("//input[@name=\"password\"]")).send_keys(("jasmin123"))
driver.find_element_by_xpath(('//button[@type="submit"]')).click()
sleep(3)

#driver.find_element_by_xpath(("//button[contains(text(),'Not Now')]")).click()
sleep(3)
driver.find_element_by_xpath(("//button[contains(text(),'Not Now')]")).click()
sleep(3)
driver.find_element_by_xpath(("//button[contains(text(),'Not Now'])")).click()

for i in range(3):
    for i in range(5):
        driver.find_element_by_xpath(("//button[text()='Follow']")).click()
        #sleep(1)
    driver.refresh()
