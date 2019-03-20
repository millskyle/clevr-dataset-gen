import glob
import sys
import numpy as np
import pickle
from shared import scenes



labels = [i.split('/')[-1] for i in glob.glob("../output/images/*")]

summary = []
for scene in scenes:
    for label in labels:
        files = glob.glob("../output/images/{}/*{}*.png".format(label,scene))
        summary.append([scene, label, len(files)])


summary = sorted(summary, key=lambda x:x[2])


if sys.argv[1] == "SET":
    starting_dict = {}

    for identifier in summary:
        key = identifier[0] + identifier[1]
        print(key)
        starting_dict[key] = identifier[2]
        #print("{}\t{}\t{}".format(*identifier))

    with open('.tmp','w') as F:
        pickle.dump(starting_dict, F)

else:
    with open(".tmp",'r') as F:
        starting_dict = pickle.load(F)

    for identifier in summary:
        key = identifier[0] + identifier[1]
        count = identifier[2] - starting_dict[key]
        if count > 0:
            print("{0:14}{1:6}{2:10}".format(identifier[0], identifier[1], count))


