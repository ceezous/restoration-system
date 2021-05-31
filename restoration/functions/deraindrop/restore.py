import cv2
import numpy as np
import os
import torch
from .models.generator import Generator

# the function will overwrite the image at img_dir with a new image
def restore(img_path, isTesting=False):
    # preload model and params
    model = Generator().cuda()
    dir_path, file_name= os.path.split(os.path.abspath(__file__))
    model.load_state_dict(torch.load(os.path.join(dir_path, "weights/gen.pkl")))

    # load image
    img = cv2.imread(img_path)
    print("img original shape: ", img.shape)

    # align image to a multiple of 4
    H = int(img.shape[0] / 4) * 4
    W = int(img.shape[1] / 4) * 4
    img = img[0:H, 0:W]

    # normalization
    img = np.array(img, dtype="float32") / 255.
    img = img.transpose((2, 0, 1))
    img = img[np.newaxis, :, :, :]
    img = torch.from_numpy(img).cuda()

    # restore
    with torch.no_grad():
        img = model(img)[-1]

    # transform shape and type back
    img = img.cpu()
    img = img.numpy().transpose(0, 2, 3, 1)
    img = img[0, :, :, :] * 255.

    # save the image
    if isTesting:
        img_path = "." + img_path.split(".")[1] + "_restored.jpg"
        print(img_path)
    cv2.imwrite(img_path, img)

if __name__ == "__main__":
    '''
        base on https://github.com/rui1996/DeRaindrop
    '''
    test_img_path = "./test_data/case1.jpg"
    restore(test_img_path, isTesting=True)