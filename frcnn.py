# -*- coding: utf-8 -*-
"""PA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F5IIHsRa-cBWsKHb1-ox-LftCq654m94
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.environ['PYTHONPATH'] += ":/content/drive/My Drive/Colab Notebooks/code/Detectron"
import sys
sys.path.insert(1,'/content/drive/My Drive/Colab Notebooks/code/Detectron')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My\ Drive/Colab\ Notebooks/dataset
# %cp *.tar.gz /content
# %cd /content

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# # !tar -xzvf Train.tar.gz
# !tar -xzvf Test_public.tar.gz
# !tar -xzvf Test_private.tar.gz

!echo "Finished tar unziping"
!ls
# %cd /content/drive/My Drive/Colab Notebooks/

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My Drive/Colab Notebooks/
# %rm -rf  code
# %mkdir code
# %cd code
!git init
!git remote add origin https://github.com/kaarthik-raja/TDL_Pass2.git
!git pull origin master

# Commented out IPython magic to ensure Python compatibility.
!ls
# %cd Detectron
!make

# !python tools/train_net.py \
#     --cfg configs/getting_started/M2.yaml \
#     OUTPUT_DIR "/content/drive/My Drive/Colab Notebooks/models/fastrcnn2"

!python tools/test_net.py \
    --cfg configs/getting_started/tutorial_1gpu_e2e_faster_rcnn_R-50-FPN.yaml \
    TEST.WEIGHTS '/content/drive/My Drive/Colab Notebooks/models/fastrcnn/train/coco_ass_train/generalized_rcnn/model_final.pkl' \
    NUM_GPUS 1
#!python tools/test_net.py --cfg configs/getting_started/tutorial_1gpu_e2e_faster_rcnn_R-50-FPN.yaml --output-dir ../../output \
#    --image-ext png --wts "/content/drive/My Drive/Colab Notebooks/models/fastrcnn/train/coco_ass_train/generalized_rcnn/model_final.pkl" ../../sample