import random
import cv2
import numpy as np


def main():
    src = cv2.imread("image/test_shape.png", cv2.IMREAD_GRAYSCALE)
    
    contours, hier = cv2.findContours(src, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    
    idx = 0
    while idx >= 0:
        c = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        
        
        cv2.drawContours(dst, contours, idx, c, cv2.LINE_4)
        idx = hier[0, idx, 0]
    
    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
