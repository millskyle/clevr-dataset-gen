import glob
import sys
import numpy as np
from shared import scenes

try:
    task=sys.argv[1]
except:
    task='PRINT'


labels = [i.split('/')[-1] for i in glob.glob("../output/images/*")]

summary = []
for scene in scenes:
    for label in labels:
        files = glob.glob("../output/images/{}/*{}*.png".format(label,scene))
        summary.append([scene, label, len(files), files])

summary = sorted(summary, key=lambda x:x[2])
np.random.shuffle(summary)


if task=='PRINT':
    for identifier in summary:
        print("{0:<15s}{1:<15s}\t{2:<15d}".format(*identifier[0:3]))

elif task=='GETWORK':
    num=256
    for identifier in summary:
        if identifier[-2] < num:
            remaining=int(np.log2(num-identifier[-2]))
            ducks,balls = [int(i) for i in identifier[1].split("-")]
            for _ in range(remaining):
                print("sbatch -J {scene}{ducks}{balls} -p cpu -c 1 ../image_generation/submit.s {ducks} {balls} {scene} {random}".format(ducks=ducks, balls=balls, scene=identifier[0], random=np.random.randint(0,9999)))

