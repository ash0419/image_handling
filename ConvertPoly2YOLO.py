import json
import os
import argparse

def convert2YOLO(json_path, file_path):
    
    label_index = {"car" : 0, "big_car" : 1, "bike" : 2}
     
    with open(json_path, 'r') as file:
        json_object = json.load(file)
        print(file_path)
        image_width = json_object["imageWidth"]
        image_height = json_object["imageHeight"]
        objects = json_object["shapes"]
        
        file_name = json_object["imagePath"].split('.')[0]
        
        f = open(file_path + "/" + file_name+".txt", 'w')
        
        for object in objects:
            if(object["label"] != "road"):
                label = label_index[object["label"]]
                x_min = min(l[0] for l in object["points"])
                x_max = max(l[0] for l in object["points"])
                y_min = min(l[1] for l in object["points"])
                y_max = max(l[1] for l in object["points"])
                
                center_x = round((x_min + x_max) / 2.0 / image_width, 8)
                center_y = round((y_min + y_max) / 2.0 / image_height, 8)
                w = round((x_max - x_min) /image_width, 8)
                h = round((y_max - y_min) /image_height, 8)
                
                f.write(str(label)+" " +str(center_x)+" " +str(center_y)+" " +str(w)+ " " +str(h) + "\n")
                
        f.close()
        
        print(file_name +".txt")
        

            

    
if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Convert labelme to YOLO")
    
    parser.add_argument('--file', type=str, help='One JSON File')
    parser.add_argument('--dir', type=str, help='JSON File Folder')
    
    args = parser.parse_args()
    
    if args.file:
        convert2YOLO(args.file)
    
    if args.dir:
        for file in os.listdir(args.dir):
            if(file.split(".")[-1] == "json"):
                convert2YOLO(args.dir + "/" +file, args.dir)
    
