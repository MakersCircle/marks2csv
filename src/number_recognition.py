# this module is used to identify the numbers written in each cell using the model generated
from src import table_extraction
import numpy as np
# from tensorflow.keras import models as tf
from keras import models as tf
import cv2
import os

# Get the absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the model directory
model_dir = os.path.join(current_dir, '..', 'model')

# Load the models using the absolute paths
type_model_path = os.path.join(model_dir, 'type_model.keras')
digit_model_path = os.path.join(model_dir, 'digit_model.keras')
half_model_path = os.path.join(model_dir, 'half_model.keras')


type_model = tf.load_model(type_model_path)
digit_model = tf.load_model(digit_model_path)
half_model = tf.load_model(half_model_path)


def prepare_image_array(image_array):
    if len(image_array.shape) == 3:
        img_gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = image_array
    img_resized = cv2.resize(img_gray, (40, 40))
    img_array = img_resized.astype('float32')
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array


def type_predictor(new_image):
    predictions = type_model.predict(new_image)
    classes = ['Single Digit', 'Halves', 'None']
    predicted_class = classes[np.argmax(predictions, axis=1)[0]]
    confidence = np.max(predictions, axis=1)[0]
    return predicted_class, confidence


def digit_predictor(new_image):
    predictions = digit_model.predict(new_image)
    classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'none']
    predicted_class = classes[np.argmax(predictions, axis=1)[0]]
    confidence = np.max(predictions, axis=1)[0]
    return predicted_class, confidence


def half_predictor(new_image):
    predictions = half_model.predict(new_image)
    classes = ['0.5', '1.5', '2.5', '3.5', '4.5', '5.5', '6.5', '7.5', '8.5', '9.5']
    predicted_class = classes[np.argmax(predictions, axis=1)[0]]
    confidence = np.max(predictions, axis=1)[0]
    return predicted_class, confidence


def recognise(cells: dict[int, list[np.ndarray]]) -> dict[int, list[list]]:
    results = {}
    for question_num, sub_questions in cells.items():
        sub_question_results = []
        for img_array in sub_questions:
            prepared_image = prepare_image_array(img_array)
            prediction, confidence = type_predictor(prepared_image)
            if prediction == 'Single Digit':
                prediction, confidence = digit_predictor(prepared_image)
            elif prediction == 'Halves':
                prediction, confidence = half_predictor(prepared_image)
            sub_question_results.append([prediction, float(confidence)])
        results[question_num] = sub_question_results
    return results


if __name__ == '__main__':
    img = cv2.imread('../test_images/warpped/scanned1.jpg')
    a = table_extraction.segment(img)
    print(recognise(a))
