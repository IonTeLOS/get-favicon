# get-favicon
Download a high resolution favicon for any website, easily \n
Requirements: pip install requests favicon \n
Example how to call this program: python3 get-favicon.py https://debian.org debian-favicon ~/Downloads 
or using the executable from the Releases section: get-favicon https://debian.org debian-favicon ~/Downloads 
Above commands will download a favicon for the website of https://debian.org, the file will be named debian-favicon (+whatever icon extension is downloaded) and the output directory will be the user's Downloads folder. One file of the highest possible resolution is downloaded.
Possible output of .ico files is converted to multiple resolution .png files (with the use of icoutils - not included)
