import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# Load and preprocess data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalize the images

# Define the model
model = Sequential([
    Flatten(input_shape=(28, 28)),       # Flatten 28x28 images to 1D vectors
    Dense(128, activation='relu'),       # First hidden layer with 128 neurons and ReLU activation
    Dense(64, activation='relu'),        # Second hidden layer with 64 neurons and ReLU activation
    Dense(10, activation='softmax')      # Output layer with 10 neurons for 10 classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Test Accuracy: {accuracy}')
