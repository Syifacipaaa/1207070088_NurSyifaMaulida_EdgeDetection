import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')#Baca gambar sumber
#Konversi ke Grey
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Hilangkan Noise
img0 = cv2.GaussianBlur(gray, (3, 3), 0)
#konvolusi dengan kernel
laplacian = cv2.Laplacian(img0, cv2.CV_64F)#untuk menerapkan operator Laplacian pada citra img0.
#Tampilkan dengan Matplolib
plt.subplots(121)#untuk membuat suatu tata letak (layout) yang terdiri dari 1 baris dan 2 kolom, dengan grafik pertama (subplot) ditampilkan di posisi 1.
plt.imshow(img0, cmap= 'gray')#untuk menampilkan citra img0 dengan menggunakan peta warna (colormap) 'gray' pada suatu plot.
plt.title('Original')#Menambahkan judul
plt.xticks([]), plt.yticks([])## untuk menghilangkan tanda sumbu (ticks) pada sumbu-x dan sumbu-y dalam suatu grafik.
plt.subplots(122)#untuk membuat suatu tata letak (layout) yang terdiri dari 1 baris dan 2 kolom, dengan grafik pertama (subplot) ditampilkan di posisi 2.
plt.imshow(laplacian, cmap= 'gray')#untuk menampilkan citra img0 dengan menggunakan peta warna (colormap) 'gray' pada suatu plot.
plt.title('Laplacian')#Menambahkan judul
plt.xticks([]), plt.yticks([])# untuk menghilangkan tanda sumbu (ticks) pada sumbu-x dan sumbu-y dalam suatu grafik.
plt.show()#Menampilkan citra