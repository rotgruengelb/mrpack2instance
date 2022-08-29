print("----------------------------------------------")
mrpackpath=(input("Enter the path of the .mrpack that you want to convert - PATH: "))
print("----------------------------------------------")
print("Enter the path where your Minecraft Instance should be located in. Example:")
mcinstancepath=(input("Input: C:/User/Jhon/Test > The Minecraft Instance will be in: C:/User/Jhon/Test/[PackName] - PATH: "))
print("----------------------------------------------")
from cgi import test
import imp
from operator import index
import random
from os import error
from turtle import down
from unicodedata import name
from urllib import request
random=(random.randint(100000,999999))
import zipfile
temppath=(str(mcinstancepath) + "/mcrtoinst_temp" + str(random))
print("----------------------------------------------")
print("Creating TemPath")
print(temppath)
print("----------------------------------------------")
print("Unziping...")
with zipfile.ZipFile(mrpackpath, 'r') as zip_ref:
    zip_ref.extractall(temppath)
print("Unziped")
print("----------------------------------------------")
#Reading modrinth.index.json and geting Modpack name
print("Geting Pack Name")
import json
with open(str(temppath) + "/modrinth.index.json", "r") as file:
  data = json.load(file)
packname = data["name"]
print(packname)
print("----------------------------------------------")
#Reading modrinth.index.json and saving Paths/Downloads
print("Reading modrinth.index.json...")
with open(str(temppath) + "/modrinth.index.json", "r") as file:
  data = json.load(file)
print("Extracting Download URLs...")
print("Extracting Download Paths...")
paths = [temppath+"\overrides\\"+file["path"] for file in data['files']]
downloads = [file["downloads"] for file in data["files"]]
print("::::::: Download Paths: :::::::")
print(paths)
print("::::::: Download URLs: :::::::")
downloads = sum(downloads, start=[])
print(downloads)
print("----------------------------------------------")
#Downloading
import time
import requests
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
print("Merging Download URLs and Download Paths")
inputs=zip(downloads,paths)
print(inputs)
print("----------------------------------------------")
def download(args):
    t0 = time.time(  )
    downloads, paths = args[0], args[1]
    try:
        r= requests.get(downloads)
        with open(paths, "wb") as f:
            f.write(r.content)
        return(downloads,time.time()-t0)
    except Exception as e:
        print("Problem downloading:", e)

t0 = time.time()
print("Downloads:")
for i in inputs:
    result=download(i)
    print('url:', result[0], 'time (s):', result[1])
print("Total download time (s):", time.time() - t0)
print("----------------------------------------------")
print("Creating Final Minecraft Instance Folder...")
#creating the final Pack Folder
import os
mcinstancepathdir = (str(mcinstancepath) + "/" + str(packname) + " MC")
try:
    os.mkdir(mcinstancepathdir)
    print("Final Minecraft Instance Folder created!")
except FileExistsError:
    print("Final Minecraft Instance Folder alredy exists!")
print("----------------------------------------------")
print("Moving all Downloaded/Overide Files to the Final Minecraft Instance Folder...")

import shutil    
source_dir = (str(temppath) + "/overrides")
target_dir = mcinstancepathdir
    
file_names = os.listdir(source_dir)
    
try:
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
        print("Moved all Downloaded/Overide Files to the Final Minecraft Instance Folder")
except Exception as e:
    print("Problem Moving Files:", e)
print("----------------------------------------------")
print("Deleting Temppath...")
shutil.rmtree(temppath)
print("Temppath deleted")
print("----------------------------------------------")
input("Press [Enter] to Exit ")