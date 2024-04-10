import cv2
import numpy as np
from matplotlib import pyplot as plt


def read() -> np.ndarray:
    """
    capture live answer script image from live feed
    Use the below code for development and then use open cv to
    """

    file_name = "original_img_1.jpg"
    image = cv2.imread(f"../test_images/original/{file_name}", cv2.COLOR_BGR2RGB)
    return image


if __name__ == "__main__":
    plt.imshow(read())
    plt.show()
