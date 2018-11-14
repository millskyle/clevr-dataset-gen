#!/bin/bash
#SBATCH -J ducky

#SBATCH -c 5
#SBATCH -t 00:10:00

module load blender

numducks=$1
numballs=$2
run=$3

for scene in vancouver mountains lake vancouver2; do 

(blender --background -noaudio --python render_images.py -- \
--height=256 \
--width=256 \
--use_gpu=1 \
--filename_prefix=${run}$RANDOM$RANDOM$RANDOM_${scene}_${numducks}_${numballs} \
--num_images=1000 \
--camera_jitter=1 \
--base_scene_blendfile="./data/base_scenes/${scene}.blend" \
--num_ducks=$numducks \
--num_balls=$numballs
#)  & 
) > /dev/null 2>&1 & 
#--save_blendfiles=1 \

done

wait


