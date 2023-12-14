import time
import os
import cv2
import numpy as np
from PIL import Image
from flask import Flask, request, redirect, render_template
from tensorflow.keras.models import load_model

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'} # format yang bisa di upload
app = Flask(__name__) # nama flask (default)
UPLOAD_FOLDER = 'static/uploads/' # path folder gambar yang di upload
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # ukuran maksimal gambar yang di upload 

# model yang digunakan
model_used= 'D:\KULIAH\SEMESTER 7\PRAKTIKUM\MODUL 6\model\model_done.h5'

def predict_result(model, run_time, probs, img):
    class_list = {'Paper': 0, 'Rock': 1, 'Scissors': 2}
    idx_pred = probs.index(max(probs))
    labels = list(class_list.keys())
    return render_template('/result.html', labels=labels,
                            probs=probs, model=model, pred=idx_pred,
                            run_time=run_time, img=img)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/")
def index():
    return render_template('/index.html', )

@app.route('/predict', methods=['POST'])
def predict():
    model = load_model(model_used)

    file = request.files["file"] #ngambil file dari form di html
    file.save(os.path.join('static', 'temp.jpg')) #simpan di temporary file
    img = cv2.cvtColor(np.array(Image.open(file)), cv2.COLOR_BGR2RGB) #BGR to RGB
    img = np.expand_dims(cv2.resize(img, (224,224)).astype('float32') / 255, axis=0) #rescale
    start = time.time() #waktu sekarang
    pred = model.predict(img)[0] # predict class
    labels = (pred > 0.5).astype(int) # kategorikal to angka
    runtimes = round(time.time()-start,4) 
    respon_model = [round(elem * 100, 2) for elem in pred]
    return predict_result('CLASS', runtimes, respon_model, 'temp.jpg')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2000)