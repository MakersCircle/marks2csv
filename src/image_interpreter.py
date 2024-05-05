from . import warping
from . import table_extraction
from . import number_recognition
import pandas as pd


class ImageInterpreter:
    def __init__(self, image):
        self.image = image
        self.warped_image = None
        self.results: dict[int, list[tuple[str, float]]] = {}
        self.marks: dict[int, list[str]] = {}
        self.confidence: dict[int, list[float]] = {}

    def format_result(self) -> None:
        for key, values in self.results.items():
            self.marks[key] = [value[0] if value[0] != 'None' else '0' for value in values]
            self.confidence[key] = [value[1] for value in values]

    def extract(self) -> None:
        """
        A pipeline for the processes:
        i) Warp the captured image.
        ii) Extract each individual cells from the table containing the handwritten marks.
        iii) Detect handwritten digit of each cell.
        """

        self.warped_image = warping.warp(self.image)
        cells = table_extraction.segment(self.warped_image)
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
