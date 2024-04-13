from src.image_interpreter import ImageInterpreter
from src.image_reader import read


def main():
    path = 'test_images/original/original_img_1.jpg'
    captured_image = read(path)
    image_analyser = ImageInterpreter(captured_image)
    image_analyser.extract()
    print(image_analyser.marks)


if __name__ == "__main__":
    main()
