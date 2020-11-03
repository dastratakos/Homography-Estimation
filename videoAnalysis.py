"""
https://www.pyimagesearch.com/2016/02/22/writing-to-video-with-opencv/
TODO: make info.txt and inlier_matches.png for each frame
"""
import argparse
from datetime import datetime
import os

import cv2
import moviepy.video.io.ImageSequenceClip as ISC
import numpy as np

import imageAnalysis
import util

def processVideo(directory, interactive=False):
    print('Processing video...')

    cap = cv2.VideoCapture(util.INPUT_PATH + os.listdir(util.INPUT_PATH)[0])
    ret, frame = cap.read()
    # TODO: only rotate when the image is incorrect
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    i = 0
    while(cap.isOpened()):
        print(f'\x1b[2K\r└──> Frame {i + 1}', end='')
        ret, next_frame = cap.read()
        if not ret: break

        next_frame = cv2.rotate(next_frame, cv2.ROTATE_90_CLOCKWISE)
        next_frame = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

        point_map, inliers = imageAnalysis.main(frame, next_frame, i, verbose=False)
        cv2.imwrite(util.FRAMES_PATH + str(i) + '.png',
                util.drawInliersOutliers(frame, point_map, inliers))

        if interactive:
            cv2.imshow('frame', frame)
            cv2.imshow('next frame', next_frame)

        frame = next_frame
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        i += 1

    print('\n\n' + ('=' * 30) + '\n')
    cap.release()
    cv2.destroyAllWindows()

def saveVideo(directory):
    print('Saving video...')
    image_files = sorted(
        [util.FRAMES_PATH + img for img in os.listdir(util.FRAMES_PATH)
            if img.endswith('.png') and img[:-4].isnumeric()],
        key=lambda x: int(x.split('/')[-1][:-4]))
    clip = ISC.ImageSequenceClip(image_files, fps=20)
    clip.write_videofile(util.OUTPUT_PATH + directory + '.mp4')

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--directory', help='image directory id',
        default='00')
    args = arg_parser.parse_args()
    
    util.INPUT_PATH += f'videos/{args.directory}/'
    util.OUTPUT_PATH += f'videos/{args.directory}/{datetime.now().strftime("%Y-%m-%d-%H%M")}/'
    util.POINT_MAPS_PATH += f'videos/{args.directory}/'
    util.FRAMES_PATH = util.OUTPUT_PATH + util.FRAMES_PATH

    os.makedirs(util.OUTPUT_PATH, exist_ok=True)
    os.makedirs(util.POINT_MAPS_PATH, exist_ok=True)
    os.makedirs(util.FRAMES_PATH, exist_ok=True)

    processVideo(args.directory)
    saveVideo(args.directory)