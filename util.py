import cv2
import numpy as np

INPUT_PATH = 'input/'
OUTPUT_PATH = 'output/'
POINT_MAPS_PATH = 'point_maps/'
FRAMES_PATH = 'frames/'

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)

def drawInliersOutliers(image, point_map, inliers):
    """
    inliers: set of (x1, y1) points
    """
    rows, cols = image.shape
    retImage = np.zeros((rows, cols, 3), dtype='uint8')
    retImage[:, :, :] = np.dstack([image] * 3)

    # Draw circles on top of the lines
    for x1, y1, x2, y2 in point_map:
        point = (int(x1), int(y1))
        color = GREEN if (x1, y1, x2, y2) in inliers else RED
        cv2.circle(retImage, point, 4, color, 1)

    return retImage

def drawMatches(image1, image2, point_map, inliers=None, max_points=1000):
    """
    inliers: set of (x1, y1) points
    """
    rows1, cols1 = image1.shape
    rows2, cols2 = image2.shape

    matchImage = np.zeros((max(rows1, rows2), cols1 + cols2, 3), dtype='uint8')
    matchImage[:rows1, :cols1, :] = np.dstack([image1] * 3)
    matchImage[:rows2, cols1:cols1 + cols2, :] = np.dstack([image2] * 3)

    small_point_map = [point_map[i] for i in np.random.choice(len(point_map), max_points)]

    # draw lines
    for x1, y1, x2, y2 in small_point_map:
        point1 = (int(x1), int(y1))
        point2 = (int(x2 + image1.shape[1]), int(y2))
        color = BLUE if inliers is None else (
            GREEN if (x1, y1, x2, y2) in inliers else RED)

        cv2.line(matchImage, point1, point2, color, 1)

    # Draw circles on top of the lines
    for x1, y1, x2, y2 in small_point_map:
        point1 = (int(x1), int(y1))
        point2 = (int(x2 + image1.shape[1]), int(y2))
        cv2.circle(matchImage, point1, 5, BLUE, 1)
        cv2.circle(matchImage, point2, 5, BLUE, 1)

    return matchImage