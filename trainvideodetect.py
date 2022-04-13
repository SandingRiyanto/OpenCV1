# import required package
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

# initialize the image data generator with rescaling
train_data_gen = ImageDataGenerator(rescale=1./255)
validation_data_gen = ImageDataGenerator(rescale=1./255)

# preprocess all train images
train_generator = train_data_gen.flow_from_directory(
    'data/train',
    target_size=(48, 48),
    batch_size=64,
    color_mode='grayscale',
    class_mode='categorical'
    )

# preprocess all test images
validation_generator = validation_data_gen.flow_from_directory(
    'data/train',
    target_size=(48, 48),
    batch_size=64,
    color_mode='grayscale',
    class_mode='categorical'
    )

# create model structure
model = Sequential()

model.add(Conv2D(32, kernel_size=(3,3), activation='rellu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3,3), activation='rellu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3,3), activation='rellu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(128, kernel_size=(3,3), activation='rellu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(25, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizers=Adam(lr=0.0001, decay=1e-6),
    metrics=['accuracy']
)

# train the CNN model
model_info = model.fit_generator(
    train_generator,
    steps_per_epoch=28709 // 64,
    epochs=50,
    validation_data=validation_generator,
    validation_steps=7178 // 64
)

# save model in .json file
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# save .h5 model
model.save_weights('model.h5')