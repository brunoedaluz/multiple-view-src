import os
import cv2
import numpy as np


def folders_mean(directory='./', size_8=False):
    """ Print per-image and overall mean/variance for all .png images under directory. """
    img_list = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.png'):
                img_list.append(os.path.join(root, filename))

    print('Will try to mean ', len(img_list), ' images.')

    acc = 0
    acc_var = 0
    n = 0
    for i, f in enumerate(img_list):
        print(f)
        image = cv2.imread(f, cv2.IMREAD_GRAYSCALE if size_8 else cv2.IMREAD_UNCHANGED)
        mean = image.mean()
        var = image.var()
        acc = acc + mean
        acc_var = acc_var + var
        n += 1
        print(mean, var, np.sqrt(var))
    all_mean = acc/n
    all_var_mean = acc_var/n
    print('Mean:', all_mean, 'Acumulator, n: ', acc, n)
    print('Mean var', all_var_mean, ' Sum var: ', acc_var, ' Std: ', np.sqrt(all_var_mean))
    return all_mean, all_var_mean


if __name__ == '__main__':
    folders_mean()
