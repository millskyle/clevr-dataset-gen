import glob


scenes = ["lake", "mountains", "vancouver", "vancouver2"]

scenes=["sunset"]

labels = [i.split('/')[-1] for i in glob.glob("../output/images/*")]

summary = []
for scene in scenes:
    for label in labels:
        files = glob.glob("../output/images/{}/*{}*.png".format(label,scene))
        summary.append([scene, label, len(files)])



summary = sorted(summary, key=lambda x:x[2])
for identifier in summary:
    print("{}\t{}\t{}".format(*identifier))
