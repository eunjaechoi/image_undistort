# image_undistort
image undistort

# Pinhole Camera Image undistort
+ python
    + input
        + image directory path
        + mode: Pinhole
        + calibration file path
            + Reference file) data/sample_calibration.json
        + save directory path
    + run
        + move
        ```
        cd image_undistort/python
        ```
        + run
        ```
        python undistort.py -i {image directory path} -c {calibration file path} -s {save directory path} -m {mode}
        ```
# Fisheye Camera Image undistort
