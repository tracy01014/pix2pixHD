from PIL import Image, ImageFile
import os
import random
import shutil


def tile(img, box, save_path):
    
    img.crop(box).save(save_path)

ImageFile.LOAD_TRUNCATED_IMAGES = True

### Split concat images (R, HE, H, E) (test) ###

# R = (0, 0, 256, 256)
# HE = (256, 0, 512, 256) 
# H = (512, 0, 768, 256)
# E = (768, 0, 1024, 256)


def split(PATH_IN, PATH_OUT, dtype):

    filelist = os.listdir(PATH_IN)
    for fn in filelist:
        if (fn.endswith(".png")):
            # name, ext = os.path.splitext(fn)
            img = Image.open(os.path.join(PATH_IN, fn))
            # R
            tile(img, (0, 0, 256, 256), os.path.join(PATH_OUT, dtype+'_label', fn))
            # HE
            tile(img, (256, 0, 512, 256), os.path.join(PATH_OUT, dtype+'_img', fn))
            # H
            tile(img, (512, 0, 768, 256), os.path.join(PATH_OUT, dtype+'_H', fn))
            # E
            tile(img, (768, 0, 1024, 256), os.path.join(PATH_OUT, dtype+'_E', fn))


# ### Extract val data from train data folder
# PATH = "/home/tracy/Documents/VSGD-Net/human_data"

# src_folder = os.path.join(PATH, "All_train")
# dst_folder = os.path.join(PATH, "All_val")

# filelist = os.listdir(src_folder)
# num_file = len(filelist)
# idx = random.sample(range(0, num_file), num_file//30)
# files_to_move = [filelist[id] for id in idx]

# for file in files_to_move:
#     src = src_folder + '/' + file
#     dst = dst_folder + '/' +  file
#     shutil.move(src, dst)


PATH_OUT = "/home/tracy/Documents/pix2pixHD/datasets/skincancer"

### Split concat images (R, HE, H, E) -- train ###
PATH_IN = "/home/tracy/Documents/VSGD-Net/human_data/All_train"
split(PATH_IN, PATH_OUT, 'train')

# ### Split concat images (R, HE, H, E) -- val ###
# PATH_IN = "/home/tracy/Documents/VSGD-Net/human_data/All_val"
# split(PATH_IN, PATH_OUT, 'val')

### Split concat images (R, HE, H, E) -- test ###
PATH_IN = "/home/tracy/Documents/VSGD-Net/human_data/All_test"
split(PATH_IN, PATH_OUT, 'test')