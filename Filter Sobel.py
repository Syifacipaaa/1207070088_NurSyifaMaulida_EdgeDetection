import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')#Baca gambar sumber

#Proses Sobel
img_sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)#untuk menerapkan operator Sobel pada citra img untuk mendeteksi gradien tepi horizontal (gradien dalam sumbu x).
img_sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)#untuk menerapkan operator Sobel pada citra img untuk mendeteksi gradien tepi horizontal (gradien dalam sumbu x).
img_sobel = img_sobelx + img_sobely#ntuk menggabungkan hasil deteksi tepi menggunakan operator Sobel pada sumbu x (img_sobelx) dan sumbu y (img_sobely).

#Plot Ouput
fig, axes= plt.subplots(4, 2, figsize=(8, 8))#untuk membuat sebuah figure (gambar) yang terdiri dari matriks subplot 4x2 dengan ukuran (lebar, tinggi) sebesar (8, 8) inci.
ax = axes.ravel()#untuk mengubah matriks axes menjadi array satu dimensi dengan menggunakan metode ravel().

ax[0].imshow(img, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[0].set_title("Citra Input")#Menambahkan Judul
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title("Histogram Citra Input")#Menambahkan Judul

ax[2].imshow(img_sobelx, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[2].set_title("Citra Output")#Menambahkan Judul
ax[3].hist(img.ravel(), bins=256)
ax[3].set_title("Histogram Citra Output")#Menambahkan Judul

ax[4].imshow(img_sobely, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[4].set_title("Citra Output")#Menambahkan Judul
ax[5].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[5].set_title("Histogram Citra Output")#Menambahkan Judul

ax[6].imshow(img_sobel, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[6].set_title("Citra Output")#Menambahkan Judul
ax[7].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[7].set_title("Histogram Citra Output")#Menambahkan Judul

fig.tight_layout()# untuk secara otomatis mengatur jarak antara subplot dalam sebuah gambar agar lebih rapi dan tidak tumpang tindih.
plt.show()#Menampilkan Citra