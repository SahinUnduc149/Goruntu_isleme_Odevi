import cv2
import numpy as np
import matplotlib.pyplot as plt
#02205076050 ŞAHİN UNDUÇ 3.SINIF 2.ÖĞRETİM

# Görüntüyü oku resime at.
resim = cv2.imread("apple.jpg")
# shape ile sınırları a değişkenine at
a = resim.shape
# resmi göster
cv2.imshow('normal resim', resim)

# BGR den Griye çevirme ve gösterme
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow('gri hali', gray)

# histogram hesapla
H = np.zeros(shape=(256, 1))
# matris a değerinde tutulur.
for i in range(a[0]):
    for j in range(a[1]):
        k = gray[i, j]
        H[k, 0] = H[k, 0] + 1

# histogramı yazdir.
plt.plot(H)
plt.show()
cv2.waitKey(0)
