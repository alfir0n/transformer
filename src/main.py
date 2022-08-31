import cv2
import numpy as np
import pyheif
from PIL import Image

# transform first to jpg
heif_file = pyheif.read('./files/lawn/IMG_0475.HEIC')
image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw",
    heif_file.mode,
    heif_file.stride,
    )
image.save('./files/out/heic-to.jpg', 'JPEG')

# paper = cv2.imread('./files/lawn-backyard-cutted-resized.jpg')
paper = cv2.imread('./files/out/heic-to.jpg')

# Coordinates that you want to Perspective Transform
pts1 = np.float32([[333, 50], [780, 50], [150, 620], [920, 620]])

# Size of the Transformed Image
pts2 = np.float32([[0, 0], [400, 0], [0, 500], [400, 500]])

# for val in pts1:
#     cv2.circle(paper, (val[0], val[1]), 5, (0, 255, 0), -1)

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(paper, M, (400, 500))
cv2.imwrite('./files/out/transformed.jpg', dst)
