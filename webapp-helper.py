import requests
import favicon
import subprocess
import sys
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

print("\n	webapp-helper is a simple command line application to get the favicon and title of any website. \n	Here is an example how to call this program: \n	webapp-helper https://debian.org debian-favicon ~/Downloads \n	The first argument you provide is the queried url \n	..the second argument is used for the image file name\n	..and the third is the directory inside which you want your newly created data stored. \n	Make sure you install package icoutils to be able to convert .ico output files to .png \n	..or at least ensure you have pkexec to be prompted about installing icoutils. \n	A new directory will be created if the one you choose does not exist. \n	This is a helper script to support webapp creation and is put together \n	..by Ion@TeLOS <teloslinux@protonmail.com> \n")

path = sys.argv[3]
if not os.path.exists(path):
   os.makedirs(path)
   print(">> new directory " + path + " is created as requested")

print("	Let's do some work now..\n ")

icons = favicon.get(sys.argv[1])
icon = icons[0]

response = requests.get(icon.url, stream=True)
with open(sys.argv[3] + '/' + sys.argv[2] + '.' + format(icon.format), 'wb') as image:
    for chunk in response.iter_content(1024):
        image.write(chunk)
        print(">> favicon saved as instructed inside folder: " + sys.argv[3])
   
if format(icon.format) == "ico":
    retval = subprocess.call(["which", "icotool"])
    if retval != 0:
        print("icotool not installed!")
        subprocess.run(["pkexec", "apt-get", "install", "icoutils", "-y"])
    subprocess.run(["icotool", "-x", "-o", sys.argv[3], sys.argv[3]+"/"+sys.argv[2]+".ico"])
    print("converted .ico file to .png or several .png images for more convenient use in Linux .desktop and saved it/them inside chosen folder: " + sys.argv[3])

url = sys.argv[1]
html_page = urlopen(url)
soup = BeautifulSoup(html_page, 'html.parser')
title = soup.title.string

with open(sys.argv[3] + "/" + "site-title.txt", "w") as file:
    file.write(title)
    print(">> website title saved in a text file inside chosen folder: " + sys.argv[3] + "\n>> Finished work, bye!")

sys.exit(0)    
    
