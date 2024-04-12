from src import image_interpreter
from src import image_reader


def main():
    path = ""
    captured_image = image_reader.read(path)
    image_analyser = image_interpreter.ImageInterpreter(captured_image)
    image_analyser.extract()
    print(image_analyser)


if __name__ == "__main__":
    main()
