import os
import ctypes
import datetime
import urllib.request


# Define some variables
img_url = "https://unsplash.it/1920/1080/?random&myRandomParam="+str(datetime.datetime.now().time())
img_name = "random.jpg" 
image_path = "C:\\Users\\vishg\\Documents\\git\\SetRandomWallpaper\\"+img_name



# Get the image from the API !
urllib.request.urlretrieve(img_url, img_name)
print ("Image downloaded successfully at "+image_path)


# Set the desktop wallpaper !
SPI_SETDESKWALLPAPER = 20 
print (ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3))