import cv2
import os
import numpy as np
from PIL import Image
import pickle

import pickle

base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, "images")


fdriverCascade = cv2.CascadeClassifier("resource\haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []
for root, dirs, files, in os.walk(img_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            lable = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            #print(lable, path)

            if not lable in label_ids:
                label_ids[lable] = current_id
                current_id += 1
            id_ = label_ids[lable]
            #print(label_ids)

            pil_image = Image.open(path).convert("L")  # convert into gray scale
            size = (1000, 1000)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            img_array = np.array(final_image, "uint8")
            #print(img_array)

            face = fdriverCascade.detectMultiScale(img_array, scaleFactor=1.1, minNeighbors=4)

            for(x,y,h,w) in face:
                region_of_interst = img_array[y:y+h, x:x+w]
                x_train.append(region_of_interst)
                y_labels.append(id_)

with open(r"C:\Users\Yunus\Desktop\UDIS\labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("Trainned_drivers_face.yml")












