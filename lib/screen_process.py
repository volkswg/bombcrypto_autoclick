import numpy as np
import cv2
from PIL import ImageGrab, Image, ImageChops
from time import sleep


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_image(img1, img2):
    img_np1 = np.array(img1.histogram())
    img_np2 = np.array(img2.histogram())
    error = np.sqrt(((img_np1 - img_np2) ** 2).mean())
    return error


def capture_screen():
    # while True:
    img1 = ImageGrab.grab(bbox=(0, 0, 850, 700))  # x, y, w, h
    print("capture 1")
    sleep(5)
    img2 = ImageGrab.grab(bbox=(0, 0, 850, 700))  # x, y, w, h
    print("capture 2")
    error = compare_image(img1, img2)
    if error < 10:
        print(error, 'All Rest')
        return 'all rest'
    else:
        print(error)
        return 'wait'

    # frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("frame", frame)
    # if cv2.waitKey(1) & 0Xff == ord('q'):
    #     break
