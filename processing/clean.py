import glob
import sys
import numpy as np
from shared import scenes
import progressbar
from scipy import ndimage
import tqdm
import os

#all_labels = [i.split('/')[-1] for i in glob.glob("../output/images/*")]
#
#bar = progressbar.ProgressBar()
#for label in bar(all_labels):
#    for scene in scenes:
#        sfiles = glob.glob("../output/images/{}/*{}*.png".format(label,scene))
#        for f in sfiles:
#            try:
#                ndimage.imread(f)
#            except:
#                print("Error reading {}".format(f))
#

bar = progressbar.ProgressBar()
try:
    sfiles = glob.glob("../output/images/*/*{}*.png".format(sys.argv[1]))
except:
    sfiles = glob.glob("../output/images/*/*.png")

from multiprocessing import Pool

def check_file(f):
    try:
        x=ndimage.imread(f, flatten=False)
        x=ndimage.imread(f, flatten=True)
    except IOError as E:
        print("Error reading {}".format(f))
        os.remove(f)




P = Pool(20)
for _ in tqdm.tqdm(P.imap_unordered(check_file, sfiles), total=len(sfiles)):
    pass
#P.map(check_file, sfiles)


