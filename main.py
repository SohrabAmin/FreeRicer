from selenium import webdriver
import os


#Create a driver to access the web
driver_path = os.getcwd() + '/geckodriver'

#Firefox
driver = webdriver.Firefox(executable_path=driver_path)


class Question:
    """
    A Question Object

    === Attributes ===
    answers: list
    """

    def __init__(self, answers):
        self.answers = answers

    def solver(self):
        pass


if __name__ == '__main__':
    pass
