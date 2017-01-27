import os
import ctypes
import urllib.request
import random



# Define some variables !
print ("Initializing")
img_url = "https://unsplash.it/1920/1080/?random"
img_name = str(int((random.random()*10**5)))+".jpg" 
img_path = "C:\\Users\\vishg\\Documents\\git\\SetRandomWallpaper\\"+img_name



# Get the image from the API !
print("Downloading image "+img_name)
urllib.request.urlretrieve(img_url, img_path)
print ("Image downloaded successfully at "+img_path)



# Set the desktop wallpaper !
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path, 3)