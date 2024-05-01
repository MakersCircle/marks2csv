from . import warping
from . import table_extraction
from . import number_recognition
import pandas as pd


class ImageInterpreter:
    def __init__(self, image):
        self.marks: dict[int, list[tuple[float, float]]] = {}
        self.image = image
        self.results = {}

    def format_result(self) -> None:
        for key, values in self.results.items():
            self.marks[key] = []
            for mark_str, confidence in values:
                try:
                    mark = round(float(mark_str), 1)
                except ValueError:
                    mark = 0.0
                try:
                    confidence = round(float(confidence), 2)
                except ValueError:
                    confidence = 0.0
                self.marks[key].append((mark, confidence))

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
