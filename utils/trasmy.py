import numpy as np
import cv2
from PIL import Image


class IMG_resize(object):
    def __init__(self, w, h):
        self.W = w
        self.H = h

    def __call__(self, IMG_clip):
        # list input
        IMG = np.array(IMG_clip)
        resized_Img = cv2.resize(IMG, (self.W, self.H), interpolation=cv2.INTER_LINEAR)
        out = Image.fromarray(resized_Img)
        return out


class CenterCrop(object):
    def __init__(self, size):
        self.size = (int(size), int(size))
        self.th = self.size[0]
        self.tw = self.size[1]

    def __call__(self, imgs):
        Images = np.array(imgs)
        h, w, c = Images.shape
        i = int(np.round((h - self.th) / 2.))
        j = int(np.round((w - self.tw) / 2.))
        out = Images[i:i + self.th, j:j + self.tw, :]
        out = Image.fromarray(out)
        return out
