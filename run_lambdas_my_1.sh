#!/bin/sh

export ROOT_DIR=$(pwd)
export PYTHONPATH="${ROOT_DIR}:${PYTHONPATH}"


python main.py test_images/cat_elya.jpeg -n_iter 3 -lambda 0.00012 &
python main.py test_images/kyiv_vdnh.png -n_iter 3 -lambda 0.00012 &

wait
