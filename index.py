from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import json

with open('config.json') as f:
    config = json.load(f)
print(config['id'])
print(config['pw'])

# config = configparser.ConfigParser()
# config.read('config.ini')

# driver = webdriver.Chrome(executable_path="./chromedriver")
# url = 'https://naver.com/'
# driver.get(url)



# WebDriverWait(driver, 10).until(
#     # driver.find_element_by_name('id').send_keys('아이디')
#     # driver.find_element_by_name('pw').send_keys('비밀번호')
#     # driver.find_element_by_id('loginBtn').click()
# )
# driver.quit()