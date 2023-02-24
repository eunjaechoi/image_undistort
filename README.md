# image_undistort
image undistort

# Pinhole Camera Image undistort
+ python
    + input
        + -i: image directory path
        + -m: mode: Pinhole
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
        python undistort.py -i {image directory path} -c {calibration file path} -s {save directory path} -m {mode}
        ```
        + ex)
        ```
        python undistort.py -i data/pinhole/ -c data/calibration.json -s data/result/ -m pinhole
        ```
# Fisheye Camera Image undistort
