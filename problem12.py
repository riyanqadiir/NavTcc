# Q12: Reading and Saving Image Files

import matplotlib.pyplot as plt

with open("original.jpg", "rb") as original:
    data = original.read()

with open("copy.jpg", "w") as copy:
    copy.write(data)


img1 = plt.imread("original.jpg")
img2 = plt.imread("copy.jpg")

plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.title("Copy")

plt.show()
