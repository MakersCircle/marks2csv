# This module will contain the code to segment each cell from the warped image.

from img2table.document import Image
from PIL import Image as PIL_img
import numpy as np
import cv2
import io


def extract_table(img: np.ndarray):
    """

    :param: Warped image.
    :return: Extracted table at 0th position.
    """

    dpi = (200, 200)
    img_bytes = io.BytesIO()
    pil_img = PIL_img.fromarray(img)
    pil_img.info["dpi"] = dpi
    pil_img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    doc = Image(img_bytes)
    extracted_tables = doc.extract_tables()
    return extracted_tables[0]


def segment(img: np.ndarray) -> dict[int, list[np.ndarray]]:
    """

    :param: Warped image.
    :return: Dictionary containing images of each cell.
    """

    table_contents = extract_table(img).content
    my_dict = {}
    cell_list = []

    if len(table_contents.keys()) == 5 and sum(len(value) for value in table_contents.values()) == 65:
        del table_contents[0], table_contents[4]

        for row in table_contents.values():
            for cell in row:
                new_img = img[cell.bbox.y1:cell.bbox.y2, cell.bbox.x1:cell.bbox.x2]
                img_arr = np.array(new_img)
                cell_list.append(img_arr)
        cell_arr = np.array(cell_list, dtype=object)
        reshaped_cell_list = cell_arr.reshape(3, 13)
        processed_cell_list = np.delete(reshaped_cell_list, 0, axis=1)

        for i in range(1, 13):
            key_list = []
            for sublist in processed_cell_list:
                key_list.append(sublist[i - 1])
            my_dict[i] = key_list

        return my_dict

    else:
        raise Exception("Table not detected!!!")


if __name__ == '__main__':
    image = cv2.imread('../test_images/warpped/warpped1.jpg')
    print(segment(image))
