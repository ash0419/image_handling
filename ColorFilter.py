import cv2
import numpy as np
import time
from pytools import average

def main():
    
    
    img = cv2.imread('image/test.jpg', cv2.IMREAD_COLOR)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
    # contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # cv2.drawContours(img, contours, 0, (0, 255, 0), 3) # 인덱스0, 파란색
    # cv2.drawContours(img, contours, 1, (255, 0, 0), 3) # 인덱스1, 초록색
    h = 1080
    w = 1920
    # c = 3
    
    # h, s, v = cv2.split(img_hsv)
    
    # lower_red1 = np.array([0, 200, 0])        # 빨강색 범위
    # upper_red1 = np.array([7, 255, 255])
    # lower_red2 = np.array([160, 200, 0])        # 빨강색 범위
    # upper_red2 = np.array([180, 255, 255])
    # low_red_mask = cv2.inRange(img_hsv, lower_red1, upper_red1)
    # upper_red_mask = cv2.inRange(img_hsv, lower_red2, upper_red2)
    
    # full_mask = low_red_mask + upper_red_mask
    
    
    # red_rec_x = []
    # red_rec_y = []
    # yellow_rec_x = []
    # yellow_rec_y = []
    # green_rec_x = []
    # green_rec_y = []
    # color = (0, 0, 0)
    
    
    st = time.time()
    # for _h in range(h):
    #     for _w in range(w):
    #         b,g,r = img[_h,_w]
    #         x = np.array([[b, g, r]])
    #         y = np.array([[0.114], [0.581], [0.299]], dtype=np.float64)
    #         img[_h,_w] = x@y
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f"operation time is, {time.time() - st}")
    
    
    #         # average = np.average(img[_h,_w])
    #         average = (np.abs(int(b)-int(g)) + np.abs(int(b)-int(r)) + np.abs(int(g)-int(r))) /3
    #         if average < 90:
    #             img[_h,_w,:] = 0
    #         else:
    #             x,y = _w, _h
    #             if x < 600:
    #                 red_rec_x.append(x)
    #                 red_rec_y.append(y)
    #             elif x < 1300:
    #                 yellow_rec_x.append(x)
    #                 yellow_rec_y.append(y)
    #             else:
    #                 green_rec_x.append(x)
    #                 green_rec_y.append(y)
            
    #         # if r <= average:
    #         #     img[_h,_w,:] = 0
    #         # b,g,r = img[_h,_w]
    #         # g_element = int(g) * int(g)
    #         # other_element = int(b) * int(r)
    #         # if g_element < other_element or r > 80 or b > 80:
    #         #     img[_h,_w,:] = 0
    
    # cv2.rectangle(img, (min(red_rec_x), min(red_rec_y)), (max(red_rec_x), max(red_rec_y)), 
    #               setColor(img[int(np.median(red_rec_y)), int(np.median(red_rec_x)), :]), 3)    
    # cv2.rectangle(img, (min(yellow_rec_x), min(yellow_rec_y)), (max(yellow_rec_x), max(yellow_rec_y)), setColor(img[int(np.median(yellow_rec_y)), int(np.median(yellow_rec_x)), :]), 3)    
    # cv2.rectangle(img, (min(green_rec_x), min(green_rec_y)), (max(green_rec_x), max(green_rec_y)), setColor(img[int(np.median(green_rec_y)), int(np.median(green_rec_x)), :]), 3)    
    
    # result = cv2.bitwise_and(img, img, mask=full_mask)
    cv2.imshow("result",img)
    # cv2.imshow("h",h)
    # cv2.imshow("s",s)
    # cv2.imshow("v",v)
    cv2.waitKey(0)
    
def bgr2gray_raw(img):
    weight = [0.11,0.59,0.3]
    h,w,c = img.shape
    rst = np.zeros((h,w),dtype = np.float)
    for _h in range(h):
        for _w in range(w):
            for _c in range(c):
                rst[_h,_w] += (weight[_c] * img[_h,_w,_c])
    return rst.astype(np.uint8)

def bgr2gray_idx(img):
    weight = [0.11,0.59,0.3]
    h,w,_ = img.shape
    rst = np.zeros((h,w),dtype = np.float)
    rst = (img[:,:,0] * weight[0]) + (img[:,:,1] * weight[1]) + (img[:,:,2] * weight[2])
    return rst.astype(np.uint8)
    
        
if __name__ == "__main__":
    main()