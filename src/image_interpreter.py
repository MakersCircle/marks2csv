import pandas as pd


class ImageInterpreter:

    def __init__(self):
        self.marks = {}

    def extract(self) -> dict[int, list[float]]:
        """
        :param: Captured image.
        :return: Dictionary containing marks of each question.
                 If mark = -1 -> Model has no confidence.
        """
        pass

    def __str__(self):
        if self.marks is None:
            print("No Marks Detected.")
        else:
            print(pd.DataFrame(self.marks))
