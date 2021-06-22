from selenium import webdriver
import time

chrome_driver_path = "D:\WORKING\softwares\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.speedtest.net/")
startTest = driver.find_element_by_css_selector(".start-text")
print(startTest.text)

startTest.click()
time.sleep(40)
try:
    resultID = driver.find_element_by_css_selector("div .result-data a")
    print(resultID.text)
    downSpeed = driver.find_element_by_css_selector("span download-speed")
    print(downSpeed.text)
    upSpeed = driver.find_element_by_css_selector("span upload-speed")
    print(upSpeed.text)
except:
    print("try failed.....")
    time.sleep(20)
    resultID = driver.find_element_by_css_selector("div .result-data a")
    print(resultID.text)
    resultID = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    print("YOUr ID:  ",resultID.text)
    downSpeed = driver.find_element_by_css_selector("span download-speed")
    print(downSpeed.text)
    upSpeed = driver.find_element_by_css_selector("span upload-speed")
    print(upSpeed.text)
time.sleep(5)
driver.quit()