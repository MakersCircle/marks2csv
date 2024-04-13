# this module is used to identify the numbers written in each cell using the model generated
from . import table_extraction
import numpy as np
from tensorflow.keras import models as tf
import cv2

type_model = tf.load_model('../model/type_model.keras')
digit_model = tf.load_model('../model/digit_model.keras')
half_model = tf.load_model('../model/half_model.keras')


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
    a = table_extraction.segment('../test_images/warpped/warpped1.jpg')
    print(recognise(a))
