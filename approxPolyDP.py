import base64
import cv2
import numpy as np

def makeAnnotDict(predictions,filename,img):
    labelMap = {
        '1'  : 'bike',
        '3'  : 'bike',
        '2'  : 'car',
        '5'  : 'big_car',
        '7'  : 'big_car',
        '100': 'road'
    }
    mask, segInfoList = predictions['panoptic_seg']
    height,width,_ = np.shape(img)
    imgData = labelme.LabelFile.load_image_file(filePath)
    encoded = base64.b64encode(imgData).decode('utf-8')
    annotDict = {
        "version": "5,1,1",
        "flags": {},
        "shapes": [],
        "imagePath": filename,
        "imageData": encoded,
        "imageHeight": height,
        "imageWidth": width
    }
    mask = mask.to('cpu').numpy()
    allowLabelList = labelMap.keys()
    remaping_ID = 0
    for seg_info in segInfoList:
        classID = seg_info['category_id']
        objID = seg_info['id']
        if str(classID) in allowLabelList:
            testMask = np.zeros((height,width),dtype=np.uint8)
            testMask[np.where(mask == objID)] = 255
            contours, _= cv2.findContours(testMask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            # _ : method에서 리턴 갯수가 정해져 있을 때 안 쓸 때 _ 표현
            for cnt in contours :
                shapeDict = {
                    "label": labelMap[str(classID)],
                    "points": [],
                    "group_id": remaping_ID,
                    "shape_type": "polygon",
                    "flags": {}
                }
                approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
                n = approx.ravel()
                i = 0
                for j in n :
                    if i % 2 == 0:
                        x = n[i]
                        y = n[i + 1]
                        shapeDict["points"].append([float(x),float(y)])
                    i = i + 1
                print(shapeDict)
                if labelMap[str(classID)] == 'road':
                    annotDict["shapes"].insert(0,shapeDict)
                else:
                    annotDict["shapes"].append(shapeDict)
            remaping_ID += 1
    return annotDict