from src.image_interpreter import ImageInterpreter
from src.image_reader import read


def main():
    captured_image = read()
    image_analyser = ImageInterpreter(captured_image)
    marks = image_analyser.extract()
    print(marks)


if __name__ == "__main__":
    main()
