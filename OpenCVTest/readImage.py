# -*- coding:utf-8 -*-

import cv2
from PIL import Image, ImageTk
import numpy as np
"""
功能：读取一张图片，并显示出来
"""
image = Image.open('D:/test/time.jpg') # 根据路径读取一张图片
data = np.array(image)
cv2.namedWindow("W") # 初始化一个名为Image的窗口
cv2.imshow("W", data) # 显示图片
cv2.waitKey(0) # 等待键盘触发事件，释放窗口
cv2.destroyAllWindows()