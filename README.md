# image_undistort
image undistort

# Pinhole or Fisheye Camera Image undistort
+ python
    + input
        + -i: image directory path
        + -c: calibration file path
            + Reference file) data/sample_calibration.json
        + -s: save directory path
    + run
        + move
        ```
        cd image_undistort/python
        ```
        + run
        ```
        python undistort.py -i {image directory path} -c {calibration file path} -s {save directory path}
        ```
        + ex)
        ```
        python undistort.py -i data/pinhole/ -c data/sample_pinhole_calibration.json -s data/result/
        python undistort.py -i data/fisheye/ -c data/sample_fisheye_calibration.json -s data/result/
        ```
