import numpy as np
import mnist
from PIL import Image
from flask import Flask, request
import requests
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD

app = Flask(__name__)

train_images = mnist.train_images()[:10000]
train_labels = mnist.train_labels()[:10000]
test_images = mnist.test_images()[:10000]
test_labels = mnist.test_labels()[:10000]

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

model = Sequential([
  Conv2D(8, 3, input_shape=(28, 28, 1), use_bias=False),
  MaxPooling2D(pool_size=2),
  Flatten(),
  Dense(10, activation='softmax'),
])

model.compile(SGD(lr=.005), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
  train_images,
  to_categorical(train_labels),
  batch_size=1,
  epochs=1,
  validation_data=(test_images, to_categorical(test_labels)),
)

@app.route("/vision", methods=['POST'])
def handle_image():
	img = request.files['image']
	language=request.form['language']
	image = Image.open(img)
	image = image.convert('L')
	image = image.resize((28, 28))
	test_image = np.array(image)
	test_image = (test_image / 255) - 0.5
	predictions = model.predict(np.expand_dims(test_image, axis=0))
	predicted_class = np.argmax(predictions)
	
	url = "http://digittotext-service:8080/numberToString"
	form_data = {
    "digit": str(predicted_class),
    "language": language
	}
	
	response = requests.post(url, data=form_data)
	
	#return {"result":str(predicted_class)}