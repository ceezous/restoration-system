import cv2
import numpy as np
import os
import torch
from .models.prenet_r import PReNet_r

def restore(img_path, isTesting=True):
    # preload model and params
    model = PReNet_r().cuda()
    dir_path, file_name= os.path.split(os.path.abspath(__file__))
    model.load_state_dict(torch.load(os.path.join(dir_path, "weights/PReNet6_r_latest.pth")))
    model.eval()

    # load image
    img = cv2.imread(img_path)

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
    img = model(img)[0]

    # transform shape and type back
    img = img.cpu()
    img = img.detach().numpy().transpose(0, 2, 3, 1)
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
    test_img_path = "./test_data/901_1.jpg"
    restore(test_img_path, isTesting=True)