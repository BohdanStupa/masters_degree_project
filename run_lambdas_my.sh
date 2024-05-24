#!/bin/sh

export ROOT_DIR=$(pwd)
export PYTHONPATH="${ROOT_DIR}:${PYTHONPATH}"


python main.py test_images/cat_elya.jpeg -n_iter 50 -lambda 0.00021 -n_clasters 6 &
python main.py test_images/kyiv_vdnh.png -n_iter 50 -lambda 0.00021 -n_clasters 6 &
python main.py test_images/rachiv.jpeg -n_iter 50 -lambda 0.00021 -n_clasters 6 &

wait

python main.py test_images/cat_elya.jpeg -n_iter 20 -lambda 0.00021 -theta 1.5 -n_clasters 6 &
python main.py test_images/kyiv_vdnh.png -n_iter 20 -lambda 0.00021 -theta 1.5 -n_clasters 6 &
python main.py test_images/rachiv.jpeg -n_iter 20 -lambda 0.00021 -theta 1.5 -n_clasters 6 &

wait

python main.py test_images/cat_elya.jpeg -n_iter 20 -lambda 0.00021 -theta 0.5 -n_clasters 6 &
python main.py test_images/kyiv_vdnh.png -n_iter 20 -lambda 0.00021 -theta 0.5 -n_clasters 6 &
python main.py test_images/rachiv.jpeg -n_iter 20 -lambda 0.00021 -theta 0.5 -n_clasters 6 &

wait

python main.py test_images/cat_elya.jpeg -n_iter 20 -lambda 0.00021 -theta 1.5 -tau 0.15 -n_clasters 6  &
python main.py test_images/kyiv_vdnh.png -n_iter 20 -lambda 0.00021 -theta 1.5 -tau 0.15 -n_clasters 6  &
python main.py test_images/rachiv.jpeg -n_iter 20 -lambda 0.00021 -theta 1.5 -tau 0.15 -n_clasters 6 &

wait

python main.py test_images/cat_elya.jpeg -n_iter 20 -lambda 0.00021 -theta 0.5 -tau 0.15 -n_clasters 6  &
python main.py test_images/kyiv_vdnh.png -n_iter 20 -lambda 0.00021 -theta 0.5 -tau 0.15 -n_clasters 6 &
python main.py test_images/rachiv.jpeg -n_iter 20 -lambda 0.00021 -theta 0.5 -tau 0.15 -n_clasters 6 &

wait

python main.py test_images/cat_elya.jpeg -n_iter 20 -lambda 0.00021 -hh 1.5 -n_clasters 6 &
python main.py test_images/kyiv_vdnh.png -n_iter 20 -lambda 0.00021 -hh 1.5 -n_clasters 6 &
python main.py test_images/rachiv.jpeg -n_iter 20 -lambda 0.00021 -hh 1.5 -n_clasters 6 &

wait

python main.py test_images/cat_elya.jpeg -n_iter 20 -lambda 0.00021 -hh 0.5 -n_clasters 6 &
python main.py test_images/kyiv_vdnh.png -n_iter 20 -lambda 0.00021 -hh 0.5 -n_clasters 6 &
python main.py test_images/rachiv.jpeg -n_iter 20 -lambda 0.00021 -hh 0.5 -n_clasters 6 &

wait