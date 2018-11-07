#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH -p shockwave
#SBATCH -t 00:10:00

module load cuda

blender --background -noaudio --python render_images.py -- --height=256 --width=256 --use_gpu=1 --min_objects=2 --max_objects=10 --num_images=10 --margin=0.05
