import numpy as np

np.set_printoptions(precision=6, suppress=True)

# create a grid of points to sample
dmd = np.vstack([d.ravel() for d in (np.mgrid[-300:300:3j, -200:200:3j])])
print(dmd)

true_transformation = np.asarray([[2, 0], [0, 2], [20, 0]]).T
print(true_transformation)


def augment(matrix):
    return np.vstack((matrix, np.ones(matrix.shape[1])))


# Augment the matrix with a column of ones to provide offset/translation
dmd_aug = augment(dmd)
print(true_transformation.shape, dmd.shape, dmd_aug.shape)
# for now consider the camera points with no noise
cam = true_transformation @ dmd_aug
print("")
print(cam)

# Fit a linear transform
fit_transform = np.linalg.lstsq(augment(dmd).T, cam.T, rcond=None)[0].T
print(fit_transform)
# print(fit_transform.shape)
