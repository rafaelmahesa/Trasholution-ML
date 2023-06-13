import cv2
import io
import numpy as np
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image

model = tf.keras.models.load_model("/code/app/model/model-waste_classification-v2_2.h5")
class_name=('Electronic Waste', 'Food Scraps', 'Glass', 'Metalic Materials', 'Organic Vegetation Waste', 'Paper', 'Plastic', 'Textile')
app = FastAPI()

def preprocess_input(image):
    np_image = np.asarray(image).astype('float64')
    np_image = cv2.resize(np_image, (300,300))
    np_image /= 127.5
    np_image -= 1.
    np_image = np.expand_dims(np_image, axis=0)
    return np_image

@app.get("/")
def read_root():
    return {"Message": "Hello World"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    data = await file.read()
    image = Image.open(io.BytesIO(data))
    prep_image = preprocess_input(image)
    pred = model.predict(prep_image)
    predi = int(pred.argmax(axis=1))
    result=class_name[predi]
    return result