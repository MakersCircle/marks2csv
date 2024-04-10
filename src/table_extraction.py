# This module will contain the code to segment each cell from the warped imaage.

from img2table.document import Image
import numpy as np
import cv2


def extract_table(img_path):
    img = Image(src=img_path)
    extracted_tables = img.extract_tables()

    return extracted_tables[0]


def segment(image):
    table_contents = extract_table(image).content
    img = cv2.imread(image)
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
            my_dict[str(i)] = key_list

        return my_dict

    else:
        raise Exception("Table not detected!!!")


if __name__ == '__main__':
    print(segment('test_images\warpped\warpped.jpg'))
