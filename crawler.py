from selenium import webdriver
import yaml


def login():
    cred = yaml.load(open("credentials.yml"))
    usr = cred['moodle_user']['username']
    passw = cred['moodle_user']['password']

    url = 'https://moodle.technikum-wien.at/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,
    executable_path=r"C:\Users\exelt\AppData\Local\Programs\Python\Python39\Scripts\chromedriver.exe")
    driver.get(url)

    driver.find_element_by_id("username").send_keys(usr)
    driver.find_element_by_id("password").send_keys(passw)
    driver.find_element_by_id('loginbtn').click()

    return driver

def get_course_ids(chrome):
    ret = []
    counter = 0

    url = 'https://moodle.technikum-wien.at/my/'
    chrome.get(url)
    course_names = chrome.find_elements_by_class_name('fullname')
    for name in course_names:
        if counter < 8:
            ret.append(name.text)
            counter += 1
    #chrome.close()
    return ret


def provide_course_link(chrome):
    links = []
    counter = 0
    url = 'https://moodle.technikum-wien.at/my/'
    chrome.get(url)
    elems = chrome.find_elements_by_xpath('//div[@class="container p-0 lineheightnormal"]/a')
    for elem in elems:
        if counter < 8:
            links.append(elem.get_attribute('href'))
            counter += 1
    return  links


def get_course_name_from_link(chrome, links):
    pairs = []

    for link in links:
        chrome.get(link)
        name = chrome.title
        dict = {'Name': name, 'Link' : link}
        pairs.append(dict)
    return pairs