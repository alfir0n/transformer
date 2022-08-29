import cv2
import numpy as np


# transform first to jpg
img = Image(filename='./files/lawn/IMG_0475.HEIC')
img.convert('jpg')
img.save(filename='./files/out/heic-to.jpg')

# paper = cv2.imread('./files/lawn-backyard-cutted-resized.jpg')
paper = cv2.imread('./files/lawn/IMG_0475.HEIC')

# Coordinates that you want to Perspective Transform
pts1 = np.float32([[333, 50], [780, 50], [150, 620], [920, 620]])

# Size of the Transformed Image
pts2 = np.float32([[0, 0], [400, 0], [0, 500], [400, 500]])

# for val in pts1:
#     cv2.circle(paper, (val[0], val[1]), 5, (0, 255, 0), -1)

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(paper, M, (400, 500))
cv2.imwrite('./files/out/transformed.jpg', dst)
