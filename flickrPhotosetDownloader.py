#########################################################
##                                                     ##
##             --FLICKR PHOTOSET DOWNLOADER--          ##
##              --By Kyle Hampton 6.26.15--            ##
##						       ##
## To run, copy this .py file into a blank             ##
## folder. Change lines 33, 34, and 46 as noted.       ##
##						       ##
## Open a command prompt and type:                     ##
##  						       ##
#! 'python flickrPhotosetDownloader.py XXXXXXXXXX no'  !#
##						       ##
## Where "XXXXXX" is the ID number from the URL of the ##
## photoset you are trying to download. The photos will##
## then download into whatever folder the .py is saved ##
## in. If you want to delete all the photos in that    ##
## file so you can download a new album, change the    ##
## 'no' to "clear".				       ##
##						       ##
#########################################################


from sys import argv

import flickrapi
import urllib
import os

script, photosetID, clear = argv

#-- API key and initializing the API --

api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'			## PUT YOUR API KEY IN BETWEEN THE APOSTROPHES HERE
api_password = 'XXXXXXXXXXXXXXXXXXXXXX'				## PUT YOUR API SECRET IN BETWEEN THE APOSTROPHES HERE
flickr = flickrapi.FlickrAPI(api_key, api_password)

#-- extracting the photos from the gallery --

print "\n---\nExtracting all photos from photoset...\n---\n"
setPhotos = flickr.photosets.getPhotos(photoset_id = photosetID)

#-- clearing previous files if requested --

if clear == "clear":
	print "\n---\nPurging previous files...\n---\n"
	for file in os.listdir('/Users/kylehampton/Documents/python'):		## CHANGE THIS LINE TO REFLECT THE FILE YOUR .PY IS SAVED IN
		if file.endswith('.jpg'):
			os.remove(file) 

#-- downloading the photos --

print "\n---\nDownloading files...\n---\n"
errorCount = 0
for photo in setPhotos[0]:
	try:
		print "Downloading %s..." % photo.attrib['title']
		url = "https://farm%s.staticflickr.com/%s/%s_%s_b.jpg" % (photo.attrib['farm'], photo.attrib['server'], photo.attrib['id'], photo.attrib['secret'])
		image=urllib.URLopener()
		filename = "%s.jpg" % photo.attrib['title']
		image.retrieve(url,filename)
	except IOError:
		errorCount += 1
		if errorCount > 5:
			print "There have been too many errors.\nPlease check the photoset."
			break
		else:
			print "--!-- %s failed to download, continuing to next photo..." % photo.attrib['title']


