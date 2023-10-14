# get-favicon
Download a high resolution favicon for any website and get the website's title, easily

Requirements: pip install requests favicon urllib3 bs4

webapp-helper is a simple command line application to get the favicon and title of any website

Here is an example how to call this program: 

$ webapp-helper https://debian.org debian-favicon ~/Downloads 

The first argument you provide is the queried url, the second argument is used for the image file name and the third is the directory inside which you want your newly created data stored.

Make sure you install package icoutils to be able to convert .ico output files to .png or at least ensure you have pkexec to be prompted about installing icoutils. 

A new directory will be created if the one you choose does not exist. 

To create an executable for webapp-helper create a Python virtual environment with python3 -m venv , activate it, install previously mentioned modules plus pyinstaller inside the venv and then run pyinstaller --onefile webapp-helper.py 

This is a helper script to support webapp creation and is put together by Ion@TeLOS <teloslinux@protonmail.com>
