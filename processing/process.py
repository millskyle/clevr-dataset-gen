import json
import glob
import sys
import numpy as np
from shared import scenes
import progressbar


import errno
import os


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise



try:
    task=sys.argv[1]
except:
    print("No command line arguments specified.  Only generating ducks dataset, no balls.  Specify command line arg ALL for ducks and balls")
    task='DUCKS'

np.random.seed(100) #set the seed so we get the same dataset, given the same origin files

all_labels = [i.split('/')[-1] for i in glob.glob("../output/images/*")]

files = {}
labels = {}
for split in ["train", "test"]:
    files[split] = []
    labels[split] = []

summary = []
for label in all_labels:
    if task=='DUCKS' and label[2] != "0":
        continue
    for scene in scenes:
        counter = 0
        sfiles = glob.glob("../output/images/{}/*{}*.png".format(label,scene))
        inds = np.arange(len(sfiles))
        np.random.shuffle(inds)
        test_ind = inds[0:128]
        train_ind = inds[128:1024]
        alabel = [float(i) for i in label.split("-")]
        if task=='DUCKS':
            alabel = [alabel[0]]
        for i in train_ind:
            files["train"].append(sfiles[i])
            labels["train"].append(alabel)
        for i in test_ind:
            files["test"].append(sfiles[i])
            labels["test"].append(alabel)


import h5py
from scipy import ndimage
from shutil import copyfile

if task=='DUCKS':
    of = "data/RD-1_d_{}.h5"
    odir = "data/png/RD-1/{}"
else:
    of = "data/RD-2_{}.h5"
    odir = "data/png/RD-2/{}"

img = ndimage.imread(files["test"][0])
print(img.dtype)
shape = {}
shape["train"] = [len(files["train"]),] + list(img.shape[0:2])
shape["test"] =  [len(files["test"]),] + list(img.shape[0:2])

LABEL_SIZE = 1
if task != 'DUCKS':
    LABEL_SIZE += 1

for split in ["test", "train"]:
    mkdir_p(odir.format(split))
    label_dict = {}
    for i in range(len(files[split])):
        src = files[split][i]
        filename = 'img_{}.png'.format(str(i).zfill(8))
        dst = odir.format(split) + '/' + filename
        label = [int(lll) for lll in labels[split][i]]
        label_dict[filename] = label
        print ("Copying {} to {}".format(src,dst))
        copyfile(src, dst)
    with open(odir.format(split) + '/' + "labels.json",'w') as f:
        json.dump(label_dict, f)






