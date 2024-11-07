import numpy as np
import os
from tensorflow.keras.models import load_model

predict_dict = {
    0: "Renkler",
    1: "Bej",
    2: "Beyaz",
    3: "Çok Renkli",
    4: "Gri",
    5: "Lacivert",
    6: "Mavi",
    7: "Pembe",
    8: "Siyah"
}

current_directory = os.path.dirname(os.path.abspath(__file__))
modelPath = os.path.join(current_directory, 'files', 'model.h5')
def load_ai_model(model_path=modelPath):
    return load_model(model_path)

def predict_color(model, image_array):
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions)
    return predict_dict.get(predicted_class, "Renk tahmini yapılamadı...")
