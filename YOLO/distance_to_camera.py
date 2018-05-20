# -*- coding:utf-8 -*-
import numpy as np
import cv2
def find_marker(image):
# 将图像转化为灰度值，并检测图像边缘
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    (_,cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key = cv2.contourArea)
    # 计算的区域的边界框，并返回
    return cv2.minAreaRect(c)
def distance_to_camera(knownWidth, focalLength, perWidth):
    # 计算并返回从物体到摄像头之间的距离
    return (knownWidth * focalLength) / perWidth
# 初始化物体到摄像头的已知距离
# in this case is 24 inches
KNOWN_DISTANCE = 30.0
#  初始化物体的width
KNOWN_WIDTH = 15
# 初始化图像列表（两张图像以上）
IMAGE_PATHS = ["D:/test/pig01.jpg","D:/test/pig02.jpg","D:/test/pig03.jpg"]
# 计算出focalLength
image = cv2.imread(IMAGE_PATHS[0])
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
# 遍历图像
if __name__ == "__main__":
    for imagePath in IMAGE_PATHS:
        #  下载图像，找到图像中的marker，并计算物体到摄像头的距离
        image = cv2.imread(imagePath)
        marker = find_marker(image)
        inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
        # 在画面中画一个边界框，并显示它
        box = np.int0(cv2.boxPoints(marker))
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        cv2.putText(image, "%.3fft" % (inches / 12),
                    (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                    2.0, (0, 255, 0), 3)
        cv2.imshow("image", image)
        cv2.waitKey(0)