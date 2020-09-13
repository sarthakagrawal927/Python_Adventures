import cv2
import time

first_frame = None

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
a = 1
while True:
    a += 1
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,  hierarchy) = cv2.findContours(thresh_frame.copy(),
                                          cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        (X, Y, W, H) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (X, Y), (X+W, Y+H), (0, 255, 0), 3)

    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("thresh_frame", thresh_frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
