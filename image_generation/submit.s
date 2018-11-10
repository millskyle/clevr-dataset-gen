#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH -p shockwave
#SBATCH -J ducky
#SBATCH -t 24:00:00

module load blender

numducks=$1
scene=$2


for balls in 0 1 2 3 4 5; do

(blender --background -noaudio --python render_images.py -- \
--height=256 \
--width=256 \
--use_gpu=1  \
--filename_prefix=${scene}_${numducks}_${balls} \
--num_images=1000 \
--camera_jitter=1 \
--base_scene_blendfile="./data/base_scenes/${scene}.blend" \
--num_ducks=$numducks \
--num_balls=$balls
#--save_blendfiles=1 \
) &  

done
wait

