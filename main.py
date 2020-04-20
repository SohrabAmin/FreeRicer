import selenium

#Create a driver to access the web
d = 'Driver'

class Question:
    """
    A Question Object

    === Attributes ===
    answers: list
    """

    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def solver(self):
        """
        Looks at question attribute in Question object and
        provides solution from answers attribute
        """
        pass


if __name__ == '__main__':
    q = Question('8 x 11', ['66', '88', '87', '23'])
    q.solver() == 88
