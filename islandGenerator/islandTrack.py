"""Generate image and annotations of island data."""

import os
import datetime
import shutil
from PIL import Image
import numpy as np
import yaml
from fileConvert import fileConvert


def GenerateImageData(width, height, loc, r=-1, noise_max=1):
    """
    Generate data and annotations for one image.

    Will width x height image matrix with a random number of islands in the
    range [0, max_island] and num_islands x 4 matrix of annotations specified
    as a bounding box coordinates of xmin, ymin, xmax, ymax.
    """
    w, h = width, height

    # Set sane defaults for maxium radius
    if (r < 0):
        r = min(w/4-1, h/4-1)

    # Make sure the generated circles will not engulf the image
    assert (r < w/2 and r < h/2), (
        "Maximum radius is too large for image dimensions.")

    # Initialize data with some noise
    data = np.random.random((h, w)) * noise_max

    # TODO Add random eccentricity to circles
    # random coords
    X = loc[0]
    Y = loc[1]

    # Set annotation data
    annotations = np.zeros(4)
    annotations[0] = Y - np.ceil(r)
    annotations[1] = X - np.ceil(r)
    annotations[2] = Y + np.ceil(r)
    annotations[3] = X + np.ceil(r)

    # Update image data
    xx, yy = np.mgrid[:h, :w]
    circle = (xx - X) ** 2 + (yy - Y) ** 2
    data[circle < r**2] = data[circle < r**2]+0.4
    return data, annotations


def GenerateImages(config):
    """Generate images from yaml config."""
    # Read parameters
    num_images = config['num_images']
    w = config['width']
    h = config['height']
    r_max = config['max_radius']
    noise_max = config['max_noise']

    # Generate image data
    print("Generating images...")
    x = np.random.randint(0,h)
    for i in range(num_images):
        y = int(i * (h/num_images))
        data, annotations = GenerateImageData(w, h, [x,y], r_max, noise_max)
        np.savetxt("annotations/island_{0:04d}.csv".format(i), annotations,
                   fmt='%d', delimiter=",",
                   header=str(annotations.shape[0]), comments='')
        fileConvert("annotations/island_{0:04d}.csv".format(i),
                    outDir=os.path.join(os.getcwd(), 'annotations'), delim=",",
                    headerLines=1, imageTag='.tif', imgSize=[w, h])
        data = (data*255).astype('uint8')
        im = Image.fromarray(data,mode='L')
        im.save("images/island_{0:04d}.tif".format(i))
        os.remove("annotations/island_{0:04d}.csv".format(i))
    print("Done!")


def CreateFolders():
    """Create folders for data."""
    def safeMake(dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def safeRemake(dir):
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)

    cwd = os.getcwd()
    now = datetime.datetime.now()
    dataDir = os.path.join(cwd, 'dataFolder')
    # safeRemake(dataDir)
    runDir = os.path.join(dataDir, "run%d%d%d_%d%d%d" %
                          (now.year, now.month, now.day,
                           now.hour, now.minute, now.second))
    safeMake(runDir)
    annDir = os.path.join(runDir, 'annotations')
    imDir = os.path.join(runDir, 'images')
    safeMake(annDir)
    safeMake(imDir)
    os.chdir(runDir)
    return


if __name__ == "__main__":
    with open("config.yml", 'r') as ymlfile:
        config = yaml.safe_load(ymlfile)
    CreateFolders()
    GenerateImages(config)
