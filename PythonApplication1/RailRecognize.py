import os
import numpy as np
np.random.seed(56732)
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
import keras.callbacks as callbacks
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator


def Main(*args, **kwargs):
    train_dir = 'D:/Temp/ChallengeDataset/train/'

    num_epochs = 1
    batch_size = 128

    np.load

    data_gen = ImageDataGenerator(rescale=1. / 255, validation_split=0.1)

    train_generator = data_gen.flow_from_directory(train_dir,
                                               target_size=(1400, 1400),
                                               batch_size=batch_size,
                                               class_mode='categorical', subset='training', color_mode='grayscale')

    validation_generator = data_gen.flow_from_directory(train_dir,
                                               target_size=(1400, 1400),
                                               batch_size=batch_size,
                                               class_mode='categorical', subset='validation', color_mode='grayscale')
    
    model = Sequential()

    model.add(Convolution2D(batch_input_shape=(None, 1400, 1400, 1),
            filters=256,
            kernel_size=7,
            strides=3,
            padding='same',     
            data_format='channels_first',))

    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=2,
            strides=2,
            padding='same',    
            data_format='channels_first',))

    model.add(Convolution2D(filters=256, 
            kernel_size=5, 
            strides=3, 
            padding='same', 
            data_format='channels_first'))

    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=2,
            strides=2,
            padding='same',
            data_format='channels_first',))

    model.add(Convolution2D(filters=256, 
            kernel_size=3, 
            strides=2, 
            padding='same', 
            data_format='channels_first'))

    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=2,
            strides=2,
            padding='same',    # Padding method
            data_format='channels_first',))

    model.add(Flatten())

    model.add(Dense(256))

    model.add(Activation('relu'))

    model.add(Dense(2))

    model.add(Activation('softmax'))

    adam = Adam(lr=1e-4)

    model.compile(optimizer=adam,
            loss='categorical_crossentropy',
            metrics=['accuracy'])

    if os.path.exists('SuCNN.h5'):
        model.load_weights('SuCNN.h5')