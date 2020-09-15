#!/bin/bash
python train.py \
    --opt adam \
    --lr 1e-3 \
    --gamma 1e-1 \
    --epoch 800 \
    --stage 1 \
    --weight_decay 0 \
    --gpu 0