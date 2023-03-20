import cv2
import os


def makeVideo(image_folder:str):
    video_name = 'video.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name,
                            cv2.VideoWriter_fourcc(*'DIVX'),
                            30,
                            (width, height))

    i:int = 0
    for image in images:
        print(i)
        video.write(cv2.imread(os.path.join(image_folder, image)))
        i = i +1
    
    cv2.destroyAllWindows()
    video.release()
    print("Done!")


if __name__ == "__main__":
    image_folder = 'C:/Users/shahn/Desktop/2023-02-28-14H42M57S (2)'
    makeVideo(image_folder)
