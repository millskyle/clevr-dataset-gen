#!/bin/bash
#SBATCH --mem=2G
#SBATCH -t 00:10:00
#SBATCH -p cpu
#SBATCH --nodelist=arcee

module load blender



blender --background -noaudio --python render_images.py -- \
--height=256 \
--width=256 \
--use_gpu=1 \
--filename_prefix=ex \
--num_images=10 \
--base_scene_blendfile="./data/base_scene.blend" 


