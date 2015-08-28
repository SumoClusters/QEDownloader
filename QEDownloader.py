__author__ = 'harry'

from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time


def main():
    print("         Welcome to Questa Downloader!")
    print("This will allow you to download PDF files from ITT Tech!")
    print("We will need your Login credentials to proceed.")
    print("  We will destroy the credentials upon use, don't worry.")
    username = input("Login: ")
    password = input("Password: ")
    whatclass = int(input("Type what row your class is listed:  "))
    # reclass = re.escape(whatclass)
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    driver = webdriver.Firefox()
    print("Travelling to Distance Education ITT Tech")
    driver.get('http://distance-education.itt-tech.edu/')
    login = driver.find_element_by_name("fblogincd")
    lpass = driver.find_element_by_name("fbpassword")
    login.send_keys(username)
    lpass.send_keys(password)
    del login
    del lpass
    driver.find_element_by_css_selector("input#sImage1").click()
    print("Logging in...")
    time.sleep(8)
    links = driver.find_elements_by_class_name("CLiKSTdLnkB")
    print("Finding your class...")
    links[whatclass].click()
    booktitle = driver.find_element_by_class_name("CLiKSLpNrmlLnk_Ebook").text
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'n')
    driver.switch_to.window(driver.window_handles[-1])
    print("Getting number of Pages...")
    driver.get('https://www.amazon.com')
    driver.find_element_by_css_selector("input#twotabsearchtextbox.nav-input").send_keys(booktitle)
    driver.find_element_by_css_selector("input[type=submit]").click()
    driver.find_element_by_class_name("s-access-image").click()
    time.sleep(2)
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    preg = re.compile('\s\d{3}\s')
    pages = soup.find(text=preg)
    non_decimal = re.compile(r'\D+')
    truepages = re.sub(non_decimal, '', pages)
    print(truepages)
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'w')
    """
    print("Starting to print the pages")
    # after amazon gets done with finding page count
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_class_name("CLiKSLpNrmlLnk_Ebook").click()
    time.sleep(8)
    driver.switch_to.window(driver.window_handles[-1])
    for i in pages:
        begin = 0
        driver.find_element_by_css_selector("button.submit_lt_gray.print-button").click()
"""
if __name__ == '__main__':
    main()


"""
    Credits
    https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup
    https://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python
    https://stackoverflow.com/questions/9611139/beautifulsoup-keyerror-issue
    https://stackoverflow.com/questions/13113954/selenium-webdriver-using-switch-to-windows-and-printing-the-title-doesnt-prin
    https://stackoverflow.com/questions/13247479/how-to-extract-the-text-between-some-anchor-tags
    https://addons.mozilla.org/en-US/firefox/addon/fastest-search/
    http://www.amazon.com/Getting-Started-Beautiful-Soup-Vineeth/dp/1783289554/ref=sr_1_1?ie=UTF8&qid=1440788739&sr=8-1&keywords=getting+started+with+beautiful+soup
    https://stackoverflow.com/questions/22650506/how-to-get-rid-of-non-alphanumeric-characters-at-the-beginning-or-end-of-a-strin
"""