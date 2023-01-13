import numpy as np
import cv2
# a = np.arange(10)
# print(a)
def bgr2gray_idx(img):
    weight = [0.11,0.59,0.3]
    h,w,_ = img.shape
    rst = np.zeros((h,w),dtype = np.float)
    print(rst)
    rst = (img[:,:,0] * weight[0]) + (img[:,:,1] * weight[1]) + (img[:,:,2] * weight[2])
    return rst.astype(np.uint8)

def redDetection(img_hsv):
    lower_red1 = np.array([0, 200, 0])        # 빨강색 범위
    upper_red1 = np.array([7, 255, 255])
    lower_red2 = np.array([160, 200, 0])        # 빨강색 범위
    upper_red2 = np.array([180, 255, 255])
    low_red_mask = cv2.inRange(img_hsv, lower_red1, upper_red1)
    upper_red_mask = cv2.inRange(img_hsv, lower_red2, upper_red2)
    full_mask = low_red_mask + upper_red_mask
    return full_mask
# print(np.where(a < 5, a, 10*a))
if __name__ == "__main__":
    
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    
    
    while cv2.waitKey(33) < 0:
        ret, frame = capture.read()
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = redDetection(frame2)
        
        # result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("VideoFrame", mask)
        cv2.imshow("origin", frame)

    capture.release()
    cv2.destroyAllWindows()



