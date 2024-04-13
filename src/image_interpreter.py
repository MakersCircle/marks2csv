from . import warping
from . import table_extraction
from . import number_recognition

import numpy as np
import pandas as pd


class ImageInterpreter:
    def __init__(self, image):
        self.marks: dict[int, list[float]] = {}
        self.image: np.ndarray = image
        self.results = {}

    def format_result(self) -> None:

        for key, values in self.results.items():
            self.marks[key] = []
            for mark_str, _ in values:
                try:
                    mark = float(mark_str)
                    if mark.is_integer():
                        mark = int(mark)
                except ValueError:
                    mark = 0
                self.marks[key].append(mark)

    def extract(self) -> None:
        """
        A pipeline for the processes:
        i) Warp the captured image.
        ii) Extract each individual cells from the table containing the handwritten marks.
        iii) Detect handwritten digit of each cell.
        """

        warped_image = warping.warp(self.image)
        cells = table_extraction.segment(warped_image)
        self.results = number_recognition.recognise(cells)
        self.format_result()

    def __str__(self):
        """
        Display the mark of a single answer sheet
        """
        if not self.marks:
            return "No Marks Detected."
        else:
            return pd.DataFrame(self.marks).to_string()
