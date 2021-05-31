from django.shortcuts import render
from pathlib import Path
from .models import Image
import cv2
import functions.deraindrop.restore as deraindrop
import functions.derain.restore as derain
import functions.dehaze.restore as dehaze
# import functions.oldphotorestoration.restore as oldphotorestoration
import os
import logging

BASE_DIR = Path(__file__).resolve().parent


def index(request):
    context = {
        "restore_state": False,
    }
    if request.method == "POST":

        if "upload" in request.POST:
            img_file = request.FILES.get("img")
            img = Image()
            img.name = img_file.name
            img.input_img = img_file
            img.output_img = img_file
            img.save()
            context["img"] = img
            print("---> img type: ", type(img))

        elif "restore" in request.POST:
            img = Image.objects.last()
            img_path = img.output_img.url[1:].replace('\\', '/')
            print("---> img_path is: ", img_path)

            # 根据不同类型处理图片
            r_type = request.POST["restore_type"]
            # if type == "oldphotorestoration":
            #     oldphotorestoration.oldPhotoRestoration()

            if r_type == "deraindrop":
                deraindrop.restore(img_path)

            if r_type == "derain":
                derain.restore(img_path, isTesting=False)
            
            if r_type == "dehaze":
                dehaze.restore(img_path, isTesting=False)


            # 将处理后的img文件存入context
            context["img"] = img
            # print("---> r_type: ", request.POST["restore_type"])
            context["restore_state"] = True
            pass

        elif "download" in request.POST:
            pass

    return render(request, "index.html", context)

def oldPhotoRestoration(request):
    context = {}
    return render(request, "oldphotorestoration.html", context)

def deRainDrop(request):
    context = {}
    return render(request, "deraindrop.html", context)

def deRain(request):
    context = {}
    return render(request, "derain.html", context)

def deHaze(request):
    context = {}
    return render(request, "dehaze.html", context)