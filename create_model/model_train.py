import os
import json
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import f1_score

with open('train/_annotations.coco.json') as f:
    data = json.load(f)
    
print("veri yükleme işlemi başlatıldı...")
def load_data(json_path, img_dir):
    with open(json_path) as f:
        data = json.load(f)

    # Görüntü id'lerini anahtar olarak kullanan bir sözlük oluşturalım
    image_id_to_info = {image['id']: image for image in data['images']}

    images = []
    labels = []

    for item in data['annotations']:
        img_id = item['image_id']
        img_info = image_id_to_info.get(img_id)

        if img_info is None:
            continue  # Veri seti üzerindeki ilgili görüntü bulunamadıysa dahi döngüye devam edeceğiz...

        img_name = img_info['file_name']
        img_path = os.path.join(img_dir, img_name)

        # Görüntüyü yükle ve yeniden boyutlandır
        image = Image.open(img_path).resize((128, 128))
        images.append(np.array(image))

        # Etiketi al
        labels.append(item['category_id'])

    return np.array(images), np.array(labels)

train_images, train_labels = load_data('train/_annotations.coco.json', 'train/')
valid_images, valid_labels = load_data('valid/_annotations.coco.json', 'valid/')
test_images, test_labels = load_data('test/_annotations.coco.json', 'test/')
train_images = train_images / 255.0
valid_images = valid_images / 255.0
test_images = test_images / 255.0

print("Veriler başarıyla yüklendi...")

# Modelimizi oluşturalım
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D((2, 2)),
    Dropout(0.25),  # Birinci dropout katmanı: overfitting problemi yaşamamak için dropout ekliyoruz
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),  # İkinci dropout katmanı
    
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.5),  # Üçüncü dropout katmanı

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),  # Çıktı katmanı için de dropout kullanıyoruz
    Dense(9, activation='softmax')  # Çıkış katmanı
])

print("Model oluşturuldu...")

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss',
                               patience=5,
                               restore_best_weights=True)
print("Eğitim başladı...")
history = model.fit(train_images, train_labels, epochs=50, validation_data=(valid_images, valid_labels), callbacks=[early_stopping])
print("Eğitim tamamlandı...")

# Modelimizi test veri setimiz ile test edelim ve dopruluk oranına bakalım...
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'Test accuracy: {test_acc}')

# Performans metriklerinden biri olan ve çokca kullanılan f1-score sonucumuzu da görelim.
y_pred = model.predict(test_images)
# Eğer tahminler olasılıklar olarak geldiyse, sınıf etiketlerine dönüştürelim
y_pred_classes = np.argmax(y_pred, axis=1)
f1 = f1_score(test_labels, y_pred_classes, average='weighted')
print(f"F1 Score: {f1}")

model.save("model.h5")