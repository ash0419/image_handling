import cv2
import numpy as np
import math

def main():
    src = cv2.imread("image/test_shape.png", cv2.IMREAD_COLOR)
    gray_src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    _, src_bin = cv2.threshold(gray_src, 0, 255, cv2.THRESH_OTSU)

    # 객체 검출 부분
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(
        src_bin)

    '''
    retval : label 갯수
    stats : 각 객체의 바운딩 박스, 픽셀 개수 정보를 담은 행렬
    centroids : 각 객체의 무게 중심 위치 정보를 담은 행렬
    '''

    # for i in range(1, retval):
    #     x, y, w, h, area = stats[i]
            
    #     cv2.line(src, (int(centroids[i][0]), int(centroids[i][1])), (int(centroids[i][0]), int(centroids[i][1])), (0, 0, 255), 3)
    #     cv2.rectangle(src, (x, y, w, h), (0, 0, 255))
        
    print(stats[4])
        
       
    # 꼭지점 검출
    corners = cv2.goodFeaturesToTrack(gray_src, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)
    
    object1 = []
    object2 = []
    object3 = []
    object4 = []
    if corners is not None:
        for i in range(corners.shape[0]):
            pt = (int(corners[i, 0, 0]), int(corners[i, 0, 1]))
            if(pt[0] >= 44 and pt[0] <= 184 and pt[1] >= 48 and pt[1] <= 130 ):
                object1.append(pt)
            if(pt[0] >= 332 and pt[0] <= 405 and pt[1] >= 55 and pt[1] <= 166 ):
                object2.append(pt)
            if(pt[0] >= 280 and pt[0] <= 341 and pt[1] >= 270 and pt[1] <= 355 ):
                object3.append(pt)
            if(pt[0] >= 17 and pt[0] <= 123 and pt[1] >= 318 and pt[1] <= 382 ):
                object4.append(pt)
                
            # cv2.circle(src, pt, 2, (0,0,255), 2)
            
    object1.sort(key=lambda p: math.atan2(p[1]-int(centroids[1][1]), p[0] - int(centroids[1][0])))

    for i in range(len(object1)):
        object1[i] = list(object1[i])
    
    points = np.array(list(object1), np.int32)
    print(points)
    cv2.polylines(src, [points], True, (0,0,255), 2)
    
    # threshold1 = 100
    # threshold2 = 360
    # edge_img = cv2.Canny(src, threshold1, threshold2)

    # corners = cv2.goodFeaturesToTrack(src, 400, 0.01, 10)

    # dst1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    # find_object(gray_src)
    

    # cv2.imshow('src', edge_img)
    # cv2.imshow('dst1', dst1)
    # cv2.imshow('dst2', dst2)
    # cv2.imshow("src", src)
    cv2.imshow("gray_src", src)
    cv2.waitKey(0)


def find_object(gray_img):
    height, width = gray_img.shape

    for _height in range(height):
        for _width in range(width):
            if(gray_img[_height, _width] > 200):
                print("height : " + str(_height))
                print("width : " + str(_width))


if __name__ == "__main__":
    main()
