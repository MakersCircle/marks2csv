import warping
import table_extraction
import number_recognition

import pandas as pd
from IPython.display import display


class ImageInterpreter:
    def __init__(self, image):
        self.marks = {}
        self.image = image

    def extract(self) -> dict[int, list[float]]:
        """

        :param: Captured image.
        :return: Dictionary containing marks of each question.
        """

        warped_image = warping.warp(self.image)
        cells = table_extraction.segment(warped_image)
        self.marks = number_recognition.recognise(cells)

        return self.marks

    def __str__(self):
        if self.marks is None:
            print("No Marks Detected.")
        else:
            display(pd.DataFrame(self.marks))
