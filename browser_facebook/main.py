from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import platform

facebook_https_prefix = "https://"
driver = None
words = []

def safe_find_element_by_id(driver, elem_id):
    try:
        return driver.find_element_by_id(elem_id)
    except NoSuchElementException:
        return None
def find_element_by_text(text):
    pass

def get_words(namefile = 'search_words.txt'):
    with open(namefile) as f:
        return f.read().split('\n')

def search_word(word,date=None,filters=None):
    fb_path = facebook_https_prefix + "www.facebook.com/search/posts/?q=" + word
    driver.get(fb_path)

    all_show = driver.find_element_by_xpath("//*[contains(text(), 'Доступно всем')]")
    el = all_show
    while el.tag_name != 'a':
        el = el.find_element_by_xpath('..')
    el.click()

    #set date
    if date:
        date_link = driver.find_element_by_xpath("//*[contains(text(), 'Выберите дату...')]")
        date_link.click()
        inputs = date_link.find_element_by_xpath('..').find_elements_by_tag_name('input')
        driver.execute_script("arguments[0].value = arguments[1]';", inputs[-2],date[1])
        inputs[-1].find_element_by_xpath('..').click()
        year_ul = driver.find_element_class_name('__MenuItem').find_element_by_xpath('..').find_element_by_xpath("//*[contains(text(), '{}')]".forma(date[0]))
        el = year_ul
        while el.tag_name != 'a':
            el = el.find_element_by_xpath('..')
        el.click()
        # 2019 2018 2017 2016 2015 2004
        # 0     1       2       3
    # date = ('2015','none')
    return driver.current_url.replace('www','mbasic')

def login(email, password):
    """ Logging into our own profile """
    try:
        global driver

        options = Options()

        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        # options.add_argument("headless")

        try:
            platform_ = platform.system().lower()
            chromedriver_versions = {
                "linux": "./chromedriver_linux64",
                "darwin": "./chromedriver_mac64",
                "windows": "./chromedriver_win32.exe",
            }
            driver = webdriver.Chrome(
                executable_path=chromedriver_versions[platform_], options=options
            )
        except Exception:
            print(
                "Kindly replace the Chroame Web Driver with the latest one from "
                "http://chromedriver.chromium.org/downloads "
                "and also make sure you have the latest Chrome Browser version."
                "\nYour OS: {}".format(platform_)
            )
            exit(1)

        fb_path = facebook_https_prefix + "mbasic.facebook.com/login/"
        driver.execute_script("document.body.style.zoom='40%'")
        driver.get(fb_path)
        driver.maximize_window()

        # filling the form
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("pass").send_keys(password)

        # clicking on login button
        driver.find_element_by_name("login").click()

        # if your account uses multi factor authentication
        mfa_code_input = safe_find_element_by_id(driver, "approvals_code")

        if mfa_code_input is None:
            return

        mfa_code_input.send_keys(input("Enter MFA code: "))
        driver.find_element_by_id("checkpointSubmitButton").click()

        # there are so many screens asking you to verify things. Just skip them all
        while safe_find_element_by_id(driver, "checkpointSubmitButton") is not None:
            dont_save_browser_radio = safe_find_element_by_id(driver, "u_0_3")
            if dont_save_browser_radio is not None:
                dont_save_browser_radio.click()

            driver.find_element_by_id("checkpointSubmitButton").click()

    except Exception:
        print("There's some error in log in.")
        print(sys.exc_info()[0])
        exit(1)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def get_driver():
    global driver
    return driver

def parser_post(url,likes=False,replace=False,comment=False):
    driver.get(url)
    # post_id = url.split('')
    post = {
        'url': url,
        'username' : driver.find_element_by_tag_name('h3').text,
        'text' : driver.find_element_by_tag_name('p').text,
        'likes' : driver.find_element_by_class_name('cz').text
    }
    return post

def parser_link_post(url):
    driver.get(url)
    link = driver.find_elements_by_xpath("//*[contains(text(), 'Новость целиком')]")
    # print(link)
    list_url = [l.get_attribute('href') for l in link]
    while safe_find_element_by_id(driver,'see_more_pager'):
        safe_find_element_by_id(driver, 'see_more_pager').find_element_by_tag_name('a').click()
        for l in driver.find_elements_by_xpath("//*[contains(text(), 'Новость целиком')]"):
            list_url.append(l.get_attribute('href'))
    return list_url

with open('me.txt','r') as f:
    contact = f.read().split('\n')
    email = contact[0]
    password = contact[1]

login(email,password)

url = search_word('bmw')
list_url = parser_link_post(url)

open('bmw.txt','w').close()

for url in list_url:
    post = parser_post(url)
    with open('bmw.txt','a') as f:
        f.write(post['url'] + '\n' +
                post['username'] + '\n' +
                post['text'] + '\n' +
                post['likes'] + '\n'
                )