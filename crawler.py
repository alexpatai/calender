import requests
from bs4 import BeautifulSoup
import html.parser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml

cred = yaml.load(open("credentials.yml"))
username = cred['moodle_user']['username']
password = cred['moodle_user']['password']
url = 'https://moodle.technikum-wien.at/'
options = Options()
#options.add_argument("user-data-dir=C:\\Users\patai\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
options.add_argument(r"user-data-dir=C:\Users\patai\AppData\Local\Google\Chrome\User Data\Profile 2")
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

def login(username, password):
    driver.find_element_by_id(username).send_keys(username)
    driver.find_element_by_id(password).send_keys(password)
    driver.find_element_by_id('loginbtn').click()

def get_course_ids():
    
    url = 'https://moodle.technikum-wien.at/my/'
    driver = webdriver.Chrome()
    source_code = driver.get(url)
  
    stages = driver.find_elements_by_class_name('fullname')
    print(stages)
    driver.close()

login(url, username, password)
driver.close()
#get_course_ids()