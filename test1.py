from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# pip install webdriver-manager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC





opts=webdriver.ChromeOptions()
opts.headless=True

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=opts)
driver.maximize_window()
driver.get('https://github.com/login')

# os.chdir('D:/Workspace/Projects/test2py')

#Install driver
# opts=webdriver.ChromeOptions()
# opts.headless=True

# driver = webdriver.Chrome(ChromeDriverManager().install() ,options=opts)

# driver.get("https://github.com/")
# print(driver.page_source)
# driver.quit()

driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys('sanjay.s.gunagi@gmail.com')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Me@1github')
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]').click()

# login = driver.find_element('login').send_keys('sanjay.s.gunagi@gmail.com')
# password = driver.find_element('password').send_keys('Me@1github')
# commit = driver.find_element('commit').click()


# login = driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(USERNAME)
# password = driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
# submit = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

# print(driver.page_source)

driver.get('https://github.com/GSSanjay?tab=repositories')

delay = 5 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

driver.save_screenshot("image.png")



list1=driver.find_elements(By.XPATH, '//*[@id="user-repositories-list"]/ul/li[*]/div[1]/div[1]/h3/a')
# print(list1)


for elem in list1:
    elemText=elem.get_attribute("text");
    print(elemText)