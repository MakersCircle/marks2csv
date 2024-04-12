from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def type_classifier_train():
    train_data_gen = ImageDataGenerator(rescale=1. / 255)
    test_data_gen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_data_gen.flow_from_directory(
        '../Dataset/train_set/Type',
        target_size=(40, 40),
        color_mode='grayscale',
        batch_size=32,
        class_mode='sparse',
        classes=['Single Digit','Halves','None']
    )

    test_generator = test_data_gen.flow_from_directory(
        '../Dataset/test_set/Type',
        target_size=(40, 40),
        color_mode='grayscale',
        batch_size=32,
        class_mode='sparse',
        classes=['Single Digit','Halves','None']
    )

    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(40, 40, 1)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(3, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    hist1= model.fit(train_generator, validation_data=test_generator, epochs=15)
    model.save('type_model.keras')
    print("Model Saved as type_model.keras")
    return hist1

def digit_classifier_train():
    train_data_gen = ImageDataGenerator(rescale=1. / 255)
    test_data_gen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_data_gen.flow_from_directory(
        '../Dataset/train_set/Single Digit',
        target_size=(40, 40),
        color_mode='grayscale',
        batch_size=32,
        class_mode='sparse',
        classes=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    )

    test_generator = test_data_gen.flow_from_directory(
        '../Dataset/test_set/Single Digit',
        target_size=(40, 40),
        color_mode='grayscale',
        batch_size=32,
        class_mode='sparse',
        classes=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    )
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(40, 40, 1)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    hist2=model.fit(train_generator, validation_data=test_generator, epochs=20)
    model.save('digit_model.keras')
    print("Model Saved as digit_model.keras")
    return hist2

def half_classifier_train():
    train_data_gen = ImageDataGenerator(rescale=1. / 255)
    test_data_gen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_data_gen.flow_from_directory(
        '../Dataset/train_set/Halves',
        target_size=(40, 40),
        color_mode='grayscale',
        batch_size=32,
        class_mode='sparse',
        classes=['0.5', '1.5', '2.5', '3.5', '4.5', '5.5', '6.5', '7.5', '8.5', '9.5']
    )

    test_generator = test_data_gen.flow_from_directory(
        '../Dataset/test_set/Halves',
        target_size=(40, 40),
        color_mode='grayscale',
        batch_size=32,
        class_mode='sparse',
        classes=['0.5', '1.5', '2.5', '3.5', '4.5', '5.5', '6.5', '7.5', '8.5', '9.5']
    )
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(40, 40, 1)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    hist3=model.fit(train_generator, validation_data=test_generator, epochs=20)
    model.save('half_model.keras')
    print("Model Saved as half_model.keras")
    return hist3
def graph_plot(history,labels):
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    for hist, label in zip(histories, labels):
        plt.plot(hist.history['accuracy'], label=f'Training Accuracy ({label})')
        plt.plot(hist.history['val_accuracy'], label=f'Validation Accuracy ({label})')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.subplot(1, 2, 2)
    for hist, label in zip(histories, labels):
        plt.plot(hist.history['loss'], label=f'Training Loss ({label})')
        plt.plot(hist.history['val_loss'], label=f'Validation Loss ({label})')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

if __name__ == '__main__':
    hist1=type_classifier_train()
    hist2=digit_classifier_train()
    hist3=half_classifier_train()
    graph_plot([hist1, hist2, hist3], ['Type Classifier', 'Digit Classifier', 'Half Classifier'])