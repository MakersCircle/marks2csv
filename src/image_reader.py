import cv2
import numpy as np
from matplotlib import pyplot as plt


def read(path) -> np.ndarray:
    """
    capture live answer script image from live feed
    Use the below code for development and then use open cv to
    """

    image = cv2.imread(path)
    return image


if __name__ == "__main__":
    file_name = "original_img_1.jpg"
    path = f"../test_images/original/{file_name}"
    plt.imshow(read(path))
    plt.show()
