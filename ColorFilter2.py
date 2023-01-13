import cv2
import numpy as np

def main():
    
    img_origin = cv2.imread('image/test2_traffic_lamp.jpg', cv2.IMREAD_COLOR)
    img_hsv = cv2.cvtColor(img_origin, cv2.COLOR_BGR2HSV)

    w = 740
        
    for i in range(4):
        img = img_hsv[:,int(w/4)*i:int(w/4)*(i+1),:]
        signal_list = []
        signal_list.append(redDetection(img))
        signal_list.append(yellowDetection(img))
        signal_list.append(greenDetection(img))
        
        signal_count = 0
        signal_color = []
        data = {}
        for index, signal in enumerate(signal_list):
            if signal:
                signal_count += 1
                if(index == 0):
                    signal_color.append("red")
                elif(index ==1):
                    signal_color.append("yellow")
                else:
                    signal_color.append("green")
                    
        data["index"] = i
        data["signal"] = signal_color
        data["error"] = "Error" if signal_count > 1 else "OK"
        
        print(data)
        
def redDetection(img_hsv):
    result = []
    # lower_red1 = np.array([0, 200, 0])
    # upper_red1 = np.array([9, 255, 255])
    lower_red2 = np.array([160, 200, 0])
    upper_red2 = np.array([180, 255, 255])
    # low_red_mask = cv2.inRange(img_hsv, lower_red1, upper_red1)
    upper_red_mask = cv2.inRange(img_hsv, lower_red2, upper_red2)
    # full_mask = low_red_mask + upper_red_mask
    x,y = np.where(upper_red_mask != 0)
    # cv2.imshow("img1_hsv", upper_red_mask)
    # cv2.waitKey(0)
    x,y = checkObject(x,y)
    if(x.size != 0 and y.size != 0):
        result = [[min(x), min(y)], [max(x), max(y)]]
    return result

def yellowDetection(img_hsv):
    result = []
    lower_yellow = np.array([26, 185, 0])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    x,y = np.where(yellow_mask != 0)
    x,y = checkObject(x,y)
    if(x.size != 0 and y.size != 0):
        result = [[min(x), min(y)], [max(x), max(y)]]
    return result
    
def greenDetection(img_hsv):
    result = []
    lower_green = np.array([45, 175, 0])
    upper_green = np.array([90, 255, 255])
    green_mask = cv2.inRange(img_hsv, lower_green, upper_green)
    x,y = np.where(green_mask != 0)
    x,y = checkObject(x,y)
    if(x.size != 0 and y.size != 0):
        result = [[min(x), min(y)], [max(x), max(y)]]
    return result

def checkObject(x,y):
    if(x.size < 100):
        x = np.array([], dtype=np.float64)
        y = np.array([], dtype=np.float64)
    return x, y
    
if __name__ == "__main__":
    main()