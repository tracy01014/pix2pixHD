### Using labels only
python -m torch.distributed.run --nproc_per_node 1 train.py --name R2HE_256p --dataroot './datasets/skincancer/' --no_instance 