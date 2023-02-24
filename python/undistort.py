import os
import cv2
import glob
import json
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", action="store", help="input image dir path")
parser.add_argument("-m", "--mode", action="store", help="camera mode")
parser.add_argument("-c", "--calibration", action="store", help="input calibration file path")
parser.add_argument("-s", "--save", action="store", help="save dir path")
args = parser.parse_args()


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


# input data
image_dir_path = f'{args.image}/*'
calibration_path = args.calibration

# mode
mode = args.mode

# save path
save_path = args.save

# calibration setting
cali = json.load(open(calibration_path))
intrinsicMatrix = np.array(cali['intrinsicMatrix'])
distortionCoefficients = np.array(cali['distortionCoefficients'])
rectification = np.array(cali['rectification'])
projectionMatrix = np.array(cali['projectionMatrix'])

image_path_list = glob.glob(image_dir_path)
for image_path in image_path_list:

    extension = image_path.split('/')[-1].split('.')[-1]
    if extension != 'png' and extension != 'jpg':
        continue

    file_name = image_path.split('/')[-1]

    image = cv2.imread(image_path)

    h, w, c = image.shape

    size = (w, h)

    if mode == 'pinhole' or mode == 'Pinhole':
        mapx, mapy = cv2.initUndistortRectifyMap(intrinsicMatrix, distortionCoefficients, rectification, projectionMatrix, size, cv2.CV_32FC1)

        image_remap = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

        save_file_path = f'{save_path}/{file_name}'
        cv2.imwrite(save_file_path, image_remap)