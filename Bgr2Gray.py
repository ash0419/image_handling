import cv2
import numpy as np
import time

def main():
    
    
    img = cv2.imread('image/test.jpg', cv2.IMREAD_COLOR)
    h = 1080
    w = 1920
    
    st = time.time()
    # for _h in range(h):
    #     for _w in range(w):
    #         b,g,r = img[_h,_w]
    #         x = np.array([[b, g, r]])
    #         y = np.array([[0.114], [0.581], [0.299]], dtype=np.float64)
    #         img[_h,_w] = x@y
    
    img = bgr2gray_idx(img)
    print(f"operation time is, {time.time() - st}")
    
    cv2.imshow("result",img)
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
    print(rst)
    rst = (img[:,:,0] * weight[0]) + (img[:,:,1] * weight[1]) + (img[:,:,2] * weight[2])
    return rst.astype(np.uint8)
    
        
if __name__ == "__main__":
    main()