from src import ImageInterpreter
from src import read


def main():
    path = 'test_images/original/original_img_1.jpg'
    captured_image = read(path)
    image_analyser = ImageInterpreter(captured_image)
    marks = image_analyser.extract()
    print(marks)


if __name__ == "__main__":
    main()
