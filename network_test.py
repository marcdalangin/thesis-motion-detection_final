import tensorflow as tf
from keras import layers, models

# Define the number of dense blocks and transition layers
num_dense_blocks = 4
num_transition_layers = 3
growth_rate = 32  # Number of filters added per dense block

# Define the input shape
input_shape = (32, 32, 3)
num_classes = 10  # Replace with the actual number of classes

# Build the model
model = models.Sequential()

# Initial convolutional layer
model.add(layers.Conv2D(64, kernel_size=(3, 3), padding='same', input_shape=input_shape))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))

# Add dense blocks and transition layers
num_filters = 64  # Number of filters in the current dense block

for i in range(num_dense_blocks):
    # Dense block
    for _ in range(6):  # Each dense block has 6 convolutional layers
        model.add(layers.BatchNormalization())
        model.add(layers.Activation('relu'))
        model.add(layers.Conv2D(growth_rate, kernel_size=(3, 3), padding='same'))
        model.add(layers.Dropout(0.2))

    num_filters += growth_rate

    if i < num_dense_blocks - 1:
        # Transition layer
        model.add(layers.BatchNormalization())
        model.add(layers.Activation('relu'))
        model.add(layers.Conv2D(num_filters // 2, kernel_size=(1, 1), padding='same'))
        model.add(layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(layers.Dropout(0.2))

# Global average pooling and output layers
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(128))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(num_classes, activation='softmax'))

# Print the model summary
model.summary()
model.save('test.h5')

