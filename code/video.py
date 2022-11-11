import cv2
import time
print("press 's' to save\n")
print("image save in './save'")


def video_demo():
    video_path = 0
    b=True;
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    capture = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    while 1:
        loca = time.strftime('%Y-%m-%d-%H-%M-%S')
        new_name = str(loca) + ".jpg"
        filename = "../save/" + new_name
        if b == True :
            new_name1 = str(loca)+ ".avi"
            filename1 = "../save/" + new_name1
        ret, frame = capture.read()
        if ret is not True:
            break
        cv2.imshow("frame", frame)
        c = cv2.waitKey(10)
        if c == ord('q'):
            break
        if c == ord('p'):
            b=not b
            if b == False:
                print(f"begin saving")
                a = 0
            elif b == True :
                print(f"end saving")
        if b == False :
            
            if a == 0:
                out = cv2.VideoWriter(filename1,fourcc,30.0,(640,480))
                print(f"saving")
                a = 1
            out.write(frame)
            
            #print(f"saving")
      
        if c == ord('s'):
            cv2.imwrite(filename, frame)
            print(f"save {new_name}")
    cv2.destroyAllWindows()
    capture.release()


if __name__ == "__main__":
    video_demo()
