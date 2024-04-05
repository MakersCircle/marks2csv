from src import image_interpreter
from src import image_reader


def main():
    captured_image = image_reader.read()
    image_analyser = image_interpreter.ImageInterpreter(captured_image)
    marks = image_analyser.extract()
    print(marks)


if __name__ == "__main__":
    main()
