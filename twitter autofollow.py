from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver=webdriver.Chrome(executable_path=r"C:\Users\trupt\OneDrive\Desktop\practice\MadLib\chromedriver.exe")
driver.get("https://twitter.com/login")
sleep(4)
element=driver.find_element_by_name("session[username_or_email]")
element.send_keys("jasmin.jupiter.jam@gmail.com")

element=driver.find_element_by_name("session[password]")
element.send_keys("jasmin123")

element.send_keys(Keys.RETURN)

sleep(3)

for i in range(3):

    sleep(2)
    driver.find_element_by_xpath(("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/aside/div[2]/div[3]/div/div[2]/div/div[2]/div/div/span/span")).click()
    sleep(2)
    driver.find_element_by_xpath(("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/aside/div[2]/div[2]/div/div[2]/div/div[2]/div/div/span/span")).click() 
    sleep(2)
    driver.find_element_by_css_selector(("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-zso239.r-1hycxz > div > div.css-1dbjc4n.r-gtdqiz.r-1hycxz > div > div > div > div.css-1dbjc4n.r-1uaug3w.r-1uhd6vh.r-1867qdf.r-1phboty.r-rs99b7.r-ku1wi2.r-1bro5k0.r-1udh08x > aside > div:nth-child(2) > div:nth-child(1) > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci > div > div.css-1dbjc4n.r-1n0xq6e > div > div > span > span")).click() 
    sleep(2)
    driver.refresh()


