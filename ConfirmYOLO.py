import cv2
import numpy as np
import os
import argparse


def confirmYOLO(img_path, yolo_format):
    
    src = cv2.imread(img_path, cv2.IMREAD_COLOR)
    
    h, w, _ = src.shape

    with open(yolo_format, 'r') as file:
        lines = file.readlines()

        for line in lines:
            center_x = int(float(line.split(" ")[1]) * w)
            center_y = int(float(line.split(" ")[2]) * h)
            width = int(float(line.split(" ")[3]) * w)
            height = int(float(line.split(" ")[4].replace("\n", "")) * h)

            cv2.rectangle(src, (center_x-int(width/2), center_y+int(height/2)),
                          (center_x+int(width/2), center_y-int(height/2)), (0, 0, 255), 3)

    file.close()

    cv2.imshow(img_path, src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # confirmYOLO('./Polygon/20201010_060030-090138_S_586.jpg', './20201010_060030-090138_S_586.txt')
    parser = argparse.ArgumentParser(
        description="Confirm Converted YOLO format")

    parser.add_argument('--dir', type=str, help='Select Folder')
    args = parser.parse_args()

    ROOT_DIR = args.dir
    if ROOT_DIR:
        file_list = os.listdir(ROOT_DIR)
        file_name = set()
        for file in file_list:
            file_name.add(file.split(".")[0])

        for file in file_name:
            confirmYOLO(ROOT_DIR + file+".jpg", ROOT_DIR + file+".txt")
