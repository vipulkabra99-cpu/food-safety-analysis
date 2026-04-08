import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("food_detection_model.h5")

# Example class labels (modify based on dataset)
class_names = ["pizza", "burger", "fries", "salad"]

def predict_food(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    index = np.argmax(prediction)

    return class_names[index]