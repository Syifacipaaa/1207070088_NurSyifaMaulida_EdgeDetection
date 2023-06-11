import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')#Baca gambar sumber

#Prewit
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])#untuk mengidentifikasi perbedaan intensitas piksel antara piksel-piksel di sekitarnya.
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])#untuk mengidentifikasi perbedaan intensitas piksel antara piksel-piksel di sekitarnya.

img_prewittx = cv2.filter2D(img, -1, kernelx)#fungsi filter2D dari library OpenCV (cv2) untuk menerapkan kernel kernelx pada citra img menggunakan operasi konvolusi.
img_prewitty = cv2.filter2D(img, -1, kernely)#fungsi filter2D dari library OpenCV (cv2) untuk menerapkan kernel kernely pada citra img menggunakan operasi konvolusi.
img_prewitt = img_prewittx + img_prewitty#operasi penjumlahan antara dua citra, yaitu img_prewittx dan img_prewitty

#Plot Ouput
fig, axes= plt.subplots(4, 2, figsize=(8, 8))#untuk membuat sebuah figure (gambar) yang terdiri dari matriks subplot 4x2 dengan ukuran (lebar, tinggi) sebesar (8, 8) inci.
ax = axes.ravel()#untuk mengubah matriks axes menjadi array satu dimensi dengan menggunakan metode ravel().

ax[0].imshow(img, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[0].set_title("Citra Input")#Menambahkan Judul
ax[1].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[1].set_title("Histogram Citra Input")

ax[2].imshow(img_prewittx, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[2].set_title("Citra Output")#Menambahkan Judul
ax[3].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[3].set_title("Histogram Citra Output")#Menambahkan Judul

ax[4].imshow(img_prewitty, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[4].set_title("Citra Output")#Menambahkan Judul
ax[5].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[5].set_title("Histogram Citra Output")#Menambahkan Judul

ax[6].imshow(img_prewitt, cmap = 'gray')#untuk menampilkan citra img pada subplot pertama (indeks 0) dari array ax dengan menggunakan peta warna (colormap) 'gray'.
ax[6].set_title("Citra Output")#Menambahkan Judul
ax[7].hist(img.ravel(), bins=256)#untuk menggambar histogram dari citra img pada subplot kedua (indeks 1) dari array ax.
ax[7].set_title("Histogram Citra Output")#Menambahkan Judul

fig.tight_layout()# untuk secara otomatis mengatur jarak antara subplot dalam sebuah gambar agar lebih rapi dan tidak tumpang tindih.
plt.show()#Menampilkan Citra