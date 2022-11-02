import cv2
import numpy as np
#02205076050 ŞAHİN UNDUÇ 3.SINIF 2.ÖĞRETİM

# Resmi göster.
img2 = cv2.imread('apple.jpg')
cv2.imshow('Orijinal Resim', img2)

# İşlenecek resim.
resim = cv2.imread('apple.jpg', 0)
cv2.imshow('resim', resim)

# shape ile resim boyutunda matris oluştur
# np.zeros ile 0 ile dolu dizi dönder
# dizide gezerek inverting işlemini gerçekleştir
[h, w] = resim.shape
resim2 = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        img2[i, j] = 255 - resim[i, j]

# işlenen resmi göster
cv2.imshow("Ters resim", img2)
cv2.waitKey()
