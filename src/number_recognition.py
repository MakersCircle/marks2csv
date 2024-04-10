# this module is used to identify the numbers written in each cell using the model generated
import numpy as np


def recognise(cells: dict[int, list[np.ndarray]]) -> dict[int, list[int]]:
    """
    Recognises the handwritten marks.
    :param cells: Contain the image of each cell as dictionary where each key is the
                  question number and corresponding value will be a list containing three
                  ndarray representing images of three cells of the corresponding mark.
    :return: Dictionary were key is the question number from 1 to 12 and value will be a list
             containing marks of sub questions.
    """
    raise NotImplemented("recognise() function is yet to be implemented")


if __name__ == '__main__':
    recognise()
