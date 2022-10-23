"""
A webscrapper that automates the process of adding tech recruiters on Linkedin.
You need a premium account to have no limitations per day add quota.
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Hunting(self, search_term):
    """
    A class that automates the process of adding tech recruiters on Linkedin.
    """
    def __init__(self):
        """
        Initialize the class with links to login, and search for recruiters.
        """
        self.login_link = "https://www.linkedin.com/"
        
    def do_login(self):
        """
        Login to Linkedin.
        """
        # Open the login page.
        self.browser.get(self.login_link)
        # Find the username and password fields.
        username = self.browser.find_element_by_xpath('//*[@id="session_key"]')
        password = self.browser.find_element_by_xpath('//*[@id="session_password"]')
        # Enter the username and password.
        username.send_keys(self.username)
        password.send_keys(self.password)
        # Find the login button and click it.
        login_button = self.browser.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div/form/button')
        login_button.click()
        # Wait for the search page to load.
        self.browser.implicitly_wait(10)

    def do_search_by_people(self):
        """
        Search for based on search_term .
        """
        # Find the search field.
        search_field = self.browser.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
        # Enter the search term.
        search_field.send_keys(search_term)
        # Click enter
        search_field.send_keys(Keys.ENTER)
        # Wait for the search page to load.
        self.browser.implicitly_wait(10)
        # create for to run from 0 to 100, increasing the number inside a url string
        for page_number in range(1,101):
            # Open the page.
            page_url = f"https://www.linkedin.com/search/results/people/?keywords=tech%20recruiter&origin=SWITCH_SEARCH_VERTICAL&page={page_number}&sid=2dK"
            self.browser.get(page_url)
            # Wait for the page to load.
            self.browser.implicitly_wait(10)
            # Add the recruiters not added to your network.
            self.add_not_added_users()
            # Access next page
            page_number += 1

    def add_not_added_users(self):
        """
        Add the recruiters not added to your network.
        """
        # List how many persons with text "Conectar" are in the page.
        entire_results = self.browser.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/ul')
        lenght_to_connect_people = 
        for person in entire_results.find_elements_by_tag_name('li'):
            if person.text == "Conectar":
                # Click the "Conectar" button.
                person.find_element_by_tag_name('button').click()        
        # Wait for the page to load.
        self.browser.implicitly_wait(10)

