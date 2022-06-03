import cv2
from matplotlib import pyplot as plt


def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


img = cv2.imread('./image.jpeg')  #read image to add brightness
BrightImage = change_brightness(img, value=60) #value can range from 0 to 100


cv2.imwrite('BrightImage.jpg', BrightImage)  #save Bright Image


plt.figure()
f, axarr = plt.subplots(2,1) 
axarr[0].imshow(img)
axarr[1].imshow(BrightImage)
plt.show()