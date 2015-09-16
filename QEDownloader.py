__author__ = 'SumoClusters'
"""
    <A Program to automatically download ITTT Ebooks>
    Copyright (C) <2015>  <SumoClusters>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from selenium.webdriver.common.keys import Keys
# from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
from os.path import expanduser
import re
import time
import os
import getpass

def main():
    print("         Welcome to 'Q' Downloader!")
    print("This will allow you to download PDF files from ITTT!")
    print("Before getting started, you must log in at least once for the new Bookshelf!")
    print("We will need your Login credentials to proceed.")
    print("  We will destroy the credentials upon use, don't worry.")
    username = input("Login: ")
    password = (getpass.getpass('Please Enter a Password: '))
    whatclass = int(input("Type what row your class is listed:  "))
    whatclass -= 1
    useremail = dir(input("ter bookshelf email: "))
    bookpass = getpass.getpass("Enter your Bookshelf Password")

    home = expanduser("~")
    filen = 'a'  # base filename
    filec = 0  # filename counter
    filep = filen+str(filec)  # perfect filename
    print("Configuring Firefox Profile")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("print.always_print_silent", True)
    profile.set_preference("browser.link.open_newwindow.restriction", 0)
    print("Starting Firefox")
    driver = webdriver.Firefox(profile)
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
    print(booktitle.title())
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
    truepages = int(re.sub(non_decimal, '', pages))
    print(truepages)
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'w')

    print("Initializing Downloading Loop")
    # after amazon gets done with finding page count
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_class_name("CLiKSLpNrmlLnk_Ebook").click()
    time.sleep(8)
    driver.switch_to.window(driver.window_handles[-1])
    begin = 1
    end = 11
    filen = 'a'  # base filename
    filec = 0  # filename counterhttps://github.com/SumoClusters/QEDownloader.git
    filep = filen + str(filec) + ".pdf"  # perfect filename
    # The following doesn't work anymore with the updated interface
    """newtab = driver.find_element_by_xpath("//a[@class='solo root go']")
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(newtab) \
        .key_up(Keys.CONTROL) \
        .perform()
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'w')
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'w')
   """
    pdf = home + "/PDF"
    if not os.path.exists(pdf):
        os.mkdir(pdf)
    os.chdir(pdf)  # goes to PDF directory
    time.sleep(10)
    loop = truepages - 5
    if driver.current_url == "http://itt-tech.vitalsource.com/#/user/signin":
        driver.find_element_by_xpath("//input[@id='email-field']").send_keys(perfemail)
        driver.find_element_by_xpath("//input[@id='password-field']").send_keys(bookpass)
        driver.find_element_by_xpath("//input[@class='large-button']").click()
        time.sleep(8)
    driver.find_element_by_xpath("//button[@class='modal-x noButton']").click()
    booktitle = booktitle.title()
    while begin < loop:
            driver.switch_to.window(driver.window_handles[-1])
            print("Downloading section: " + str(begin) + " of " + str(end) + ". Out of: " + str(truepages))
            driver.find_element_by_xpath("//button[@data-tooltip='Print Pages']").click()
            driver.find_element_by_xpath("//input[@placeholder='Start']").clear()
            driver.find_element_by_xpath("//input[@placeholder='Start']").send_keys(begin)
            driver.find_element_by_xpath("//input[@id='printTo']").clear()
            driver.find_element_by_xpath("//input[@id='printTo']").send_keys(end)
            # Starts the print process
            driver.find_element_by_xpath("//button[@class='submit ']").click()
            time.sleep(25)
            driver.switch_to.window(driver.window_handles[-1])
            for filename in os.listdir(pdf):
                if filename.startswith(booktitle.split(' ', 1)[0]):
                    os.rename(filename, filep)
            filec += 1
            filep = filen + str(filec) + ".pdf"
            begin += 10
            end += 10

    print("Finished, enjoy your book! ^-^")

""""
   doesn't work I Recommend third party software to merge the the pdfs
    print("Merging to PDF")
    merger = PdfFileMerger()
    files = [x for x in os.listdir(pdf) if x.endswith(".pdf")]
    for fname in sorted(files):
        merger.append(PdfFileReader(open(os.path.join(pdf, fname), 'rb')))
    merger.write(booktitle+'.pdf')
    name = booktitle+'.pdf'
    print("Extracting Headers from penultimate PDF")
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
    https://stackoverflow.com/questions/15954682/setting-selenium-to-use-custom-profile-but-it-keeps-opening-with-default
    https://stackoverflow.com/questions/20984698/use-firefox-print-or-save-as-features-using-selenium-webdriver
    https://addons.mozilla.org/en-us/firefox/addon/element-locator-for-webdriv/
    https://stackoverflow.com/questions/27775759/send-keys-control-click-selenium
    http://michaeljaylissner.com/posts/2008/10/19/change-the-default-print-to-file-to-pdf-in-ubuntu-hardy/
    https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python
    https://stackoverflow.com/questions/2759067/rename-files-in-python
    https://stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary
    https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
    https://support.mozilla.org/en-US/questions/1035103
    https://stackoverflow.com/questions/14411028/python-printing-attributes-with-no-dict
"""