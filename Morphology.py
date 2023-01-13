import cv2
from cv2 import getStructuringElement
import numpy as np

def main():
    img = cv2.imread('image/test2_traffic_lamp.jpg', cv2.IMREAD_COLOR)

    # 영상의 가로 세로 채널수 획득하는 방법
    h, w, c = img.shape
    print('width: ', w)
    print('height: ', h)
    print('channel: ', c)

    # Img RGB to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Find Red
    lower_red = np.array([160, 200, 0])
    upper_red = np.array([180, 255, 255])
    upper_red_mask = cv2.inRange(img_hsv, lower_red, upper_red)
    
    k = getStructuringElement(cv2.MORPH_RECT, (3, 3))
    result = cv2.morphologyEx(upper_red_mask, cv2.MORPH_OPEN, k)
    
    cv2.imshow("red", upper_red_mask)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()