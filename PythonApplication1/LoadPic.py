import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


def Main(*args, **kwargs):
    #读取图像
    im = misc.imread("D:/图像识别竞赛/ChallengeDataset/train/neg/1.jpg", flatten=True)
    #显示图像
    plt.figure(0)
    plt.imshow(im)
 
    #旋转图像
    im_rotate = misc.imrotate(im, 90)
    plt.figure(1)
    plt.imshow(im_rotate)
 
    #保存图像
    misc.imsave("lena_rotate.jpg", im_rotate)

    plt.show()
    return 0


if __name__ == '__main__':
    Main()