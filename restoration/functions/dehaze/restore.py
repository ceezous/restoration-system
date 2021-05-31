import cv2
import numpy as np
import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.utils as vutils
from .models.ffanet import FFANet
from PIL import Image

# the function will overwrite the image at img_dir with a new image


def restore(img_path, isTesting=False):
    # preload model and params
    model = nn.DataParallel(FFANet()).cuda()
    dir_path, file_name= os.path.split(os.path.abspath(__file__))
    model.load_state_dict(torch.load(os.path.join(dir_path, "weights/ots_train_ffa_3_19.pk"))["model"])
    model.eval()

    # # load image
    # img = cv2.imread(img_path)

    # # align image to a multiple of 4
    # H = int(img.shape[0] / 4) * 4
    # W = int(img.shape[1] / 4) * 4
    # img = img[0:H, 0:W]

    # # normalization
    # img = np.array(img, dtype="float32") / 255.
    # img = img.transpose(2, 0, 1)
    # img = img[np.newaxis, :, :, :]
    # img = torch.from_numpy(img).cuda()

    img = Image.open(img_path)
    img = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.64, 0.6, 0.58], std=[0.14, 0.15, 0.152])
    ])(img)[None, ::]
    with torch.no_grad():
        img = model(img)
        print(img)
    img = torch.squeeze(img.clamp(0, 1).cpu())
    if isTesting:
        img_path = "." + img_path.split(".")[1] + "_restored.jpg"
        print(img_path)
    vutils.save_image(img, img_path)

    # # restore
    # with torch.no_grad():
    #     img = model(img)
    #     print(img)
    #     print("img shape after modeling: ", img.shape)

    # # transform shape and type back
    # img = img.cpu()
    # img = img.numpy().transpose(0, 2, 3, 1)
    # img = img[0, :, :, :] * 255.

    # # save the image
    # if isTesting:
    #     img_path = "." + img_path.split(".")[1] + "_restored.jpg"
    #     print("img_path: ", img_path)
    # print("write result: ", cv2.imwrite(img_path, img))


if __name__ == "__main__":
    '''
        base on *
    '''
    test_img_path = "./test_data/building.jpg"
    restore(test_img_path, isTesting=True)
