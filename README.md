# RPS - Prediction

**Rock Paper Scissors Prediction**
Proyek ini bertujuan untuk melakukan klasifikasi gambar rock, paper, dan scissors menggunakan model transfer learning VGG19. Dengan menggunakan Flask, aplikasi web ini memungkinkan pengguna untuk mengunggah gambar tangan rock, paper, dan scissors, dan kemudian memberikan prediksi dari model VGG19 terhadap gambar tersebut.

### Fitur 
* Menggunakan arsitektur VGG19 untuk klasifikasi gambar rock, paper, dan scissors.
* Aplikasi web sederhana dengan antarmuka pengguna menggunakan Flask.
* Pengguna dapat mengunggah gambar dan menerima prediksi dari model VGG19.
* Menggunakan TensorFlow dan Keras sebagai dasar untuk pemodelan dan prediksi.

**Pre-Rquirements :**

- [x] numpy
- [x] opencv-python
- [x] pillow
- [x] Flask
- [x] Tensorflow

## Dataset
Dataset yang digunakan merupakan kumpulan citra tangan paper, rock, dan scissors yang berjumlah 2520 gambar.
berikut merupakan contoh gambar dari masing masing kelas yang ada :

<img src="gambar/download.png"/>

Dataset yang ada dibagi menjadi 3 bagian menjadi data train, validation, dan test, dengan proporsi 75%:15%:10%.
Setelah itu data dilakukan beberapa augmentasi yang disesuaikan untuk menambah variasi data yang dimiliki, berikut hasil setelah dilakukan augmentasi :

<img src="gambar/download (1).png"/>

## Development Roadmap

- [x] [Kotlin](https://kotlinlang.org/)
- [x] [Keras VGG19](https://keras.io/api/applications/vgg/)
- [x] [Tensorflow Lite](https://www.tensorflow.org/lite/)


## Fitur

- [x] Rekomendasi Kesehatan
- [x] Info dan Berita Kesehatan
- [x] Cek Kesehatan Mulut (gigi & lidah) 

## Kebutuhan
* Android Studio Flamingo 2022.2.1 Patch 2
* Emulator / External Device
* Google Colab
* Jupyter Notebook
