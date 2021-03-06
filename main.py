import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def click_element(driver, xpath: str) -> None:
    """
    Find an HTML element with <xpath> and clicks it.
    """
    element = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", element)


def get_text(driver, xpath: str) -> str:
    """
    Find and Return the value of the HTML element with <xpath>
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        return element.get_attribute('innerHTML')
    except NoSuchElementException:
        print('Can Not Find element with XPATH: ' + xpath)


class Question:
    """
    A Question Object

    === Attributes ===
    answers: list
    """

    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers

    def solver(self) -> str:
        """
        Looks at question attribute in Question object and
        provides solution from answers attribute
        """
        for char in self.question:
            if 'x' == char:
                return str(eval(self.question[:-1].replace('x', '*')))
            elif ('+' == char) or ('-' == char) or ('/' == char):
                return str(eval(self.question[:-1]))


if __name__ == '__main__':
    # Create a driver to access the web
    driver_path = os.getcwd() + '/geckodriver'

    # Open Firefox Web Browser
    driver = webdriver.Firefox(executable_path=driver_path)

    # Open FreeRice.com
    driver.get('https://freerice.com/categories')

    # Click 'OK' on cookie notification
    click_element(driver, '/html/body/div[1]/div/div/div[2]/div[1]/button')

    # Click on 'Basic Math (Pre-Algebra)' icon
    click_element(driver, '/html/body/div[2]/section/div/div[1]/div/div[2]/div/div/div[7]/div[2]/div[1]')

    # Loop Forever
    while True:
        # Find the question
        question = get_text(driver, '/html/body/div[2]/section/div/div[1]/div/div/div[4]/div['
                                    '1]/div/div/div/div/div/div[1]')

        # Find the answers
        ans1 = get_text(driver, '/html/body/div[2]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[2]')
        ans2 = get_text(driver, '/html/body/div[2]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[3]')
        ans3 = get_text(driver, '/html/body/div[2]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[4]')
        ans4 = get_text(driver, '/html/body/div[2]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[5]')

        # Create question object
        q = Question(question, [ans1, ans2, ans3, ans4])

        # Select option that is correct, otherwise a random one if answer unknown
        ans_location = '/html/body/div[2]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div'
        if q.solver() in q.answers:
            click_element(driver, ans_location + "[%d]" % (q.answers.index(q.solver())+2))

        else:
            click_element(driver, ans_location + "[%d]" % random.randint(2, 5))

        # Avoid too may request error
        time.sleep(1)



