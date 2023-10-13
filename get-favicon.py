import requests
import favicon
import subprocess
import sys

print("example how to call this program: get-favicon https://debian.org debian-favicon ~/Downloads \nMake sure you install icoutils to convert .ico output files to .png")

icons = favicon.get(sys.argv[1])
icon = icons[0]

response = requests.get(icon.url, stream=True)
with open(sys.argv[3] + '/' + sys.argv[2] + '.' + format(icon.format), 'wb') as image:
    for chunk in response.iter_content(1024):
        image.write(chunk)
        
if format(icon.format) == "ico":
    retval = subprocess.call(["which", "icotool"])
    if retval != 0:
    print("icotool not installed!")
    subprocess.run(["pkexec", "apt-get", "install", "icoutils", "-y"])
    subprocess.run(["icotool", "-x", "-o", sys.argv[3], sys.argv[3]+"/"+sys.argv[2]+".ico"])
    print("converted .ico file to .png for more convenient use in Linux .desktop")

