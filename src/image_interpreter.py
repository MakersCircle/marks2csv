import pandas as pd
from IPython.display import display


class ImageInterpreter:
    def __init__(self):
        self.marks = {}

    def extract(self) -> dict[int, list[float]]:
        """
        :param: Captured image.
        :return: Dictionary containing marks of each question.
                 If mark = -1 -> Model has no confidence.
        """


    def __str__(self):
        if self.marks is None:
            print("No Marks Detected.")
        else:
            display(pd.DataFrame(self.marks))
