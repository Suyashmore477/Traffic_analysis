import numpy as np
import cv2
import winsound

face_cascade = cv2.CascadeClassifier('D:\\Project\\(car)Object detection\\car2.xml')
cap = cv2.VideoCapture("D:\\Project\\(car)Object detection\\traffVid1.mp4")

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    Alarmdetect = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    pos = (30, 30)
    fontScale = 1
    fontColor = (0, 255, 0)
    lineType = 2

    cv2.putText(img, "Vehicle Count -" + str(len(faces)), pos, font, fontScale, fontColor, lineType)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(faces) >= 7:
        Alarmdetect = 1
        pos1 = (80, 80)
        fontColor1 = (0, 0, 255)
        cv2.putText(img, str("High Road Traffic"), pos1, font, fontScale + 0.3, fontColor1, lineType)

    if Alarmdetect == 1:
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

    cv2.imshow('Traffic Video', img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
