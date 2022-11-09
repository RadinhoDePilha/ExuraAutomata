import cv2
import numpy as np

def locate_alpha(needle, haystack):
    
    # read game image
    if isinstance(haystack, str):
        haystack = cv2.imread(haystack)

    # read image needle
    needle = cv2.imread(needle, cv2.IMREAD_UNCHANGED)
    hh, ww = needle.shape[:2]

    # extract base image ad alpha channel and make alpha 3 channels
    base = needle[:,:,0:3]
    alpha = needle[:,:,3]
    alpha = cv2.merge([alpha,alpha,alpha])

    # do masked needle matching and save correlation image
    correlation = cv2.matchTemplate(haystack, base, cv2.TM_CCORR_NORMED, mask=alpha)

    # set threshold and get all matches
    threshhold = 0.95
    loc = np.where(correlation >= threshhold)
    if len(loc[0]) == 0:
        return None
    return loc

if __name__ == "__main__":
    print(locate_alpha('assets/triggers/pinksquare.png', 'assets/screenshotRed.png'))
