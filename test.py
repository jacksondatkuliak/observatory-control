import cv2

video = cv2.VideoCapture(0)
ret, frame = video.read()
jpeg = cv2.imencode('.jpg', frame)