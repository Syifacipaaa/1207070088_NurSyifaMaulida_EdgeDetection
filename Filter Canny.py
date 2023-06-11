import cv2
import numpy as np#library numpy
import matplotlib.pyplot as plt#Library Matplotlib

img = cv2.imread('flower.jpg')#Baca gambar sumber

img_canny = cv2.Canny(img, 100, 200)#untuk menerapkan deteksi tepi menggunakan algoritma Canny pada citra img dengan menggunakan threshold (ambang batas) sebesar 100 dan 200.

fig, axes= plt.subplots(2, 2, figsize=(8, 8))#untuk membuat sebuah figure (gambar) yang terdiri dari matriks subplot 2x2 dengan ukuran (lebar, tinggi) sebesar (8, 8) inci.
ax = axes.ravel()#untuk mengubah matriks axes menjadi array satu dimensi dengan menggunakan metode ravel().

ax[0].imshow(img, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[0].set_title("Citra Input")#Menambahkan Judul
ax[1].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[1].set_title("Histogram Citra Input")#Menambahkan Judul

ax[2].imshow(img_canny, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[2].set_title("Citra Output")#Menambahkan Judul
ax[3].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[3].set_title("Histogram Citra Output")#Menambahkan Judul

fig.tight_layout()# untuk secara otomatis mengatur jarak antara subplot dalam sebuah gambar agar lebih rapi dan tidak tumpang tindih.
plt.show()#Menampilkan Citra