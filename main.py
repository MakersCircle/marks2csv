from src import image_interpreter
from src import image_reader


def main():
    path = 'test_images/original/original_img_1.jpg'
    captured_image = image_reader.read(path)
    print("image loaded")
    image_analyser = image_interpreter.ImageInterpreter(captured_image)
    image_analyser.extract()
    print(image_analyser)


if __name__ == "__main__":
    main()
