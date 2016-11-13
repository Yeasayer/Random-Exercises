#Danbooru Downloader v0.3
#
# A utility to batch download images from danbooru.donmai.us based on
# tag input. It allows the results to either be downloaded to a directory
# individually, or in a compressed .zip file for easy viewing!
#
import requests, time, re, zipfile, shutil, os, tempfile
from PIL import Image, ImageFile
from io import BytesIO


def zip_check():

	answer = raw_input("Do you want the images saved in a .zip file, or as is in this directory?[y/n] ")
	if (answer == "y"):
		return True
	elif (answer == "n"):
		return False
	else:
		zip_check()

def num_check():
	imgcount = raw_input("How many images do you want downloaded?\nJust press Enter or 0 if you want as many as possible: ")
	print(imgcount,int(imgcount))
	if (int(imgcount) == 0):
		return 0
	elif (int(imgcount) > 0):
		return int(imgcount)
	else:
		num_check()


def database_dive(tags,count,zipbool):
	if (count == 0):
		json = {"tags":" ".join(tags)}
	else:
		json = {"tags":" ".join(tags),"limit":count}
	r = requests.get("https://danbooru.donmai.us/posts.json", params=json)
	imageindi = []
	for index,json_link in enumerate(r.json()):
		urladd = "https://danbooru.donmai.us%s" % json_link["large_file_url"]
		ner = requests.get(urladd)
		if ner.status_code == 200:
			imageindi.append(Image.open(BytesIO(ner.content)))
	save_us_all(imageindi,zipbool,"_".join(tags))

def save_us_all(arr,bool,tags):
	cwd = os.getcwd()
	i = 0
	if bool:
		name = "".join([tags,str(int(time.time())),".zip"])
		zf = zipfile.ZipFile(name, "w")
		for image in arr:
			filename = "image"+str(i)+"."+image.format
			image.save("/tmp/"+filename)
			zf.write("/tmp/"+filename,filename)
			os.remove("/tmp/"+filename)
			i = i+1
		zf.close()
	#else:




def start():
	print("Okay what do you want to download? Remember to use underscores\nfor tags with more than one word(ie: \"kinoshita_hideyoshi\", \"green_eyes\"):")
	tags = raw_input("Enter your tags: ")
	tags =  tags.split(" ")
	print("These are your tags:")
	for tag in tags:
		print(tag)
	imgcount = num_check()
	print(imgcount)
	zipbool = zip_check()
	print("Searching the database!")
	database_dive(tags,imgcount,zipbool)

start()