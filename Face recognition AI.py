import cv2

from deepface import DeepFace

img = cv2.imread("king.jpeg")
results = DeepFace.analyze(img, actions=('gender', 'emotion'))


print(results)