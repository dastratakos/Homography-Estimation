"""
file: imageAnalysis.py
----------------------
This is the main driver file, which implements a RANSAC algorithm for
homography estimation. The algorithm follows the one in "Multiple View Geometry
in computer vision" by Richard Hartley and Andrew Zisserman.
"""
import argparse
import copy
import csv
from datetime import datetime
import os

import cv2
import numpy as np

import util

THRESHOLD = 0.6
NUM_ITERS = 1000

def computeHomography(pairs):
    """
    Solves for the homography given any number of pairs of points. Visit
    http://6.869.csail.mit.edu/fa12/lectures/lecture13ransac/lecture13ransac.pdf
    slide 9 for more details.
    """
    A = []
    for x1, y1, x2, y2 in pairs:
        A.append([x1, y1, 1, 0, 0, 0, -x2 * x1, -x2 * y1, -x1])
        A.append([0, 0, 0, x1, y1, 1, -y2 * x1, -y2 * y1, -y1])
    A = np.array(A)

    # Singular Value Decomposition (SVD)
    U, S, V = np.linalg.svd(A)

    # V has shape (9, 9) for any number of input pairs. V[-1] is the eigenvector
    # of (A^T)A with the smalles eigenvalue. Reshape into 3x3 matrix.
    H = np.reshape(V[-1], (3, 3))

    # Normalization
    H = (1 / H.item(8)) * H
    return H

def dist(pair, H):
    """ Returns the geometric distance between a pair of points given the
    homography H. """
    # points in homogeneous coordinates
    p1 = np.array([pair[0], pair[1], 1])
    p2 = np.array([pair[2], pair[3], 1])

    p2_estimate = np.dot(H, np.transpose(p1))
    p2_estimate = (1 / p2_estimate[2]) * p2_estimate
    
    return np.linalg.norm(np.transpose(p2) - p2_estimate)

def RANSAC(point_map, threshold=THRESHOLD, verbose=True):
    if verbose: print(f'Running RANSAC with {len(point_map)} points...')
    bestInliers = set()
    homography = None
    for i in range(NUM_ITERS):
        # randomly choose 4 points from the matrix to compute the homography
        pairs = [point_map[i] for i in np.random.choice(len(point_map), 4)]

        H = computeHomography(pairs)
        inliers = {(c[0], c[1], c[2], c[3]) for c in point_map if dist(c, H) < 500}
        
        if verbose:
            print(f'\x1b[2K\r└──> iteration {i + 1}/{NUM_ITERS} ' + \
                  f'\t{len(inliers)} inlier' + ('s ' if len(inliers) != 1 else ' ') + \
                  f'\tbest: {len(bestInliers)}', end='')

        if len(inliers) > len(bestInliers):
            bestInliers = inliers
            homography = H
            if len(bestInliers) > (len(point_map) * threshold): break

    if verbose:
        print(f'\nNum matches: {len(point_map)}')
        print(f'Num inliers: {len(bestInliers)}')
        print(f'Min inliers: {len(point_map) * threshold}')

    return homography, bestInliers

def createPointMap(image1, image2, directory, verbose=True):
    """
    Creates a point map of shape (n, 4) where n is the number of matches
    between the two images. Each row contains (x1, y1, x2, y2), where (x1, y1)
    in image1 maps to (x2, y2) in image2.

    sift.detectAndCompute returns
        keypoints: a list of keypoints
        descriptors: a numpy array of shape (num keypoints, 128)
    """
    if verbose: print('Finding keypoints and descriptors for both images...')
    sift = cv2.SIFT_create()
    kp1, desc1 = sift.detectAndCompute(image1, None)
    kp2, desc2 = sift.detectAndCompute(image2, None)

    cv2.imwrite(util.OUTPUT_PATH + 'keypoints-1.png',
            cv2.drawKeypoints(image1, kp1, image1))
    cv2.imwrite(util.OUTPUT_PATH + 'keypoints-2.png',
            cv2.drawKeypoints(image2, kp2, image2))

    if verbose: print('Determining matches...')
    matches = cv2.BFMatcher(cv2.NORM_L2, True).match(desc1, desc2)

    point_map = np.array([
        [kp1[match.queryIdx].pt[0],
        kp1[match.queryIdx].pt[1],
        kp2[match.trainIdx].pt[0],
        kp2[match.trainIdx].pt[1]] for match in matches
    ])

    cv2.imwrite(util.OUTPUT_PATH + 'matches.png',
            util.drawMatches(image1, image2, point_map))

    with open(f'{util.POINT_MAPS_PATH}/{directory}-point_map.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x1', 'y1', 'x2', 'y2'])
        for line in point_map:
            writer.writerow(line)
    
    return point_map

def main(image1, image2, directory, verbose=True):
    """
    Info
    """
    point_map = None
    if f'{directory}-point_map.csv' in os.listdir(util.POINT_MAPS_PATH):
        if verbose: print('Loading saved point map...')
        point_map = np.loadtxt(
            util.POINT_MAPS_PATH + f'{directory}-point_map.csv',
            delimiter=',', skiprows=1)
    else:
        if verbose: print('Creating point map...')
        point_map = createPointMap(image1, image2, directory, verbose=verbose)
    
    homography, inliers = RANSAC(point_map, verbose=verbose)

    cv2.imwrite(util.OUTPUT_PATH + 'inlier_matches.png',
                util.drawMatches(image1, image2, point_map, inliers))

    # TODO: change to HTML?
    with open(util.OUTPUT_PATH + 'info.txt', 'w') as f:
        f.write(f'Homography:\n{str(homography)}\n\n')
        f.write(f'Num inliers: {len(inliers)}')

    return point_map, inliers

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--directory', help='image directory id',
        default='00')
    arg_parser.add_argument('-v', '--verbose',
        help='increase output verbosity', action='store_true')
    args = arg_parser.parse_args()
    
    util.INPUT_PATH += f'images/{args.directory}/'
    util.OUTPUT_PATH += f'images/{args.directory}/{datetime.now().strftime("%Y-%m-%d-%H%M")}/'
    util.POINT_MAPS_PATH += f'images/'

    image1 = cv2.imread(util.INPUT_PATH + '1.png', 0)
    assert image1 is not None, f'Invalid first image: {util.INPUT_PATH}1.png'
    image2 = cv2.imread(util.INPUT_PATH + '2.png', 0)
    assert image2 is not None, f'Invalid second image: {util.INPUT_PATH}2.png'

    os.makedirs(util.OUTPUT_PATH, exist_ok=True)
    os.makedirs(util.POINT_MAPS_PATH, exist_ok=True)

    main(image1, image2, args.directory)