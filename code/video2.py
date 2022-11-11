import cv2
import time
print("press 's' to save\n")
print("image save in './save'")


def video_demo():
    video_path = 0
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    capture = cv2.VideoCapture(video_path)
    while 1:
        loca = time.strftime('%Y-%m-%d-%H-%M-%S')
        new_name = str(loca) + ".jpg"
        filename = "../save/" + new_name
        ret, frame = capture.read()
        if ret is not True:
            break
        cv2.imshow("frame", frame)
        c = cv2.waitKey(10)
        if c == ord('q'):
            break

        if c == ord('s'):
            cv2.imwrite(filename, frame)
            print(f"save {new_name}")
    cv2.destroyAllWindows()
    capture.release()


if __name__ == "__main__":
    video_demo()
