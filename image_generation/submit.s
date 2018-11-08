#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH -p shockwave
#SBATCH -t 01:00:00

module load cuda
blender --background -noaudio --python render_images.py -- --height=256 --width=256 --use_gpu=1  --num_images=10 --base_scene_blendfile="./data/water.blend" --num_ducks=$1 --num_balls=$2
