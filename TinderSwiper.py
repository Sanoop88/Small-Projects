#you need to have tinder.com open for this and be your active page. Also, you need to install chromedriver.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'python projects/chromedriver.exe')#your path for chrome driver
driver.get('https://www.tinder.com')
time.sleep(10)
like=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]/span/svg/path')
for i in range(10)#Enter the number of custom number of likes
    like.click()
    time.sleep(2)


