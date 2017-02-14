###Obligatory License Nonsense because I like pretending that my code is worth anything.
'''
MIT License

Copyright (c) 2017 Joseph Acevedo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

### YouTube Video to Audio Converter
# Version 0.3

### Working Features
# Able to take a local directory .csv or .txt file, have the program parse it, and (hopefully) download the videos to convert to audio.
# Why I did this instead of going to the Pirate Bay or just getting it from a friend? I have no clue. I just like
# being difficult sometimes. :-/ Plus, I needed the practice and I get tired of coding with Django for less than a third-world
# wage. I'll probably forget all about this after 4 o'clock Saturday.

### Need To Fix
# - Deleting Temp Files
# - Function to curtail code reuse.
# - Adding a verbose option to possibly eliminate ffmpeg nonsense. Doesn't seem to work without it though...

### Need To Add
## Likely
# - Ability to save to a directory.
# - Ability to save a batch as a zip.
## Not So Likely
# - Ability to save playlist




import subprocess,re,os,math

from pymediainfo import MediaInfo
from pytube import YouTube

debug = True
truepath = os.getcwd()

##Pre sorted array of mp3 filerates.
mp3bitrates = [32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320]


class PyAudio():

	def DownloadVideos(self,argv):
		print("TRYING %s" %argv)
		try:
			yt = YouTube(argv)
		except:
			print("WHOOPS")
			return False
		print(yt.get_videos())
		try:
			ytvideo = yt.filter('mp4')[-1]
		except:
			print("UH-OH! I need a better error describer!")
			return False
		newstring = re.sub(r'[!\?\.%#&\(\) ^`~<>,\/\\\[\]]','',yt.filename)
		try:
			if debug == False:
				if os.path.isfile("/tmp/"+newstring+".mp4"):
					os.remove("/tmp/"+newstring+".mp4")
				ytvideo.download("/tmp/"+newstring+".mp4")
			else:
				if os.path.isfile(truepath+"/"+newstring+".mp4"):
					os.remove(truepath+"/"+newstring+".mp4")
				ytvideo.download(truepath+"/"+newstring+".mp4")
		except:
			print("There was an error in downloading %s" %yt.filename)
			return False
		return truepath+"/"+newstring+".mp4",newstring
	def ConvertVideo(self,path,name):
		media_info = MediaInfo.parse(path)
		print(path)
		for track in media_info.tracks:
			if track.track_type == "Audio":
				ourbitrate = int(math.ceil(float(track.bit_rate)/1000))
				## Answer generously stolen from SO: http://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
		ourbitrate = min(mp3bitrates, key=lambda x:abs(x-ourbitrate))
		print("\n\nThis video will be converted to audio at %skb bitrate!\n\n") %ourbitrate
		command = "ffmpeg -i "+path+" -ac 2 -vn -b:a "+str(ourbitrate)+"k "+name+".mp3"
		try:
			subprocess.call(command, shell=True)
		except:
			print("Well there goes the neighborhood!")
			return False,name
		return True,name


def startUp():
	print("Hola! Provide either a link or a .txt file prepended by -f and we'll find that muzak in a jiffy!\n Or just type exit to say goodbye!")
	fileinput = raw_input("Enter your file and file path: ")
	## Multiple files
	if re.search(r'^-f', fileinput):
		fileinput = fileinput[fileinput.index("-f")+3:]
		print(fileinput)
		try:
			thefile = open(fileinput,'r')
		except:
			print("OOPS! You seemed to have mistyped the filename or the path")
			startUp();
		thelist = re.split(r'[ ,\n]',thefile.read())
		thefile.close()
		thiswillbecool = PyAudio()
		for link in thelist:
			try:
				ourpath,vidname = thiswillbecool.DownloadVideos(link)
			except:
				print("There seems to be a problem with that link. Moving on.")
				continue
			if ourpath is not False:
				try:
					isitdone,filepath = thiswillbecool.ConvertVideo(ourpath,vidname)
				except:
					print("There seems to be an error in converting %s. Moving on.") %vidname

	###Single file
	elif re.search(r"(youtube\.com\/watch\?v=([A-Z]|[a-z]|[0-9]|[-]){1,}|youtu\.be\/([A-Z]|[a-z]|[0-9]|[-]){1,})", fileinput):
		print("Alright we're gonna go ahead any try that link")
		thiswillbecool = PyAudio()
		try:
			ourpath,vidname = thiswillbecool.DownloadVideos(fileinput)
		except:
			print("Sorry, it look like there was a error!")
		if ourpath is not False:
			try:
				isitdone,filepath = thiswillbecool.ConvertVideo(ourpath,vidname)
			except:
				print("Sorry... There seems to be an error in converting %s") %filepath

	###Cute little exit.
	elif re.search(r'^exit$',fileinput,flags=re.I):
		print("ADIOS AMIGO! ^_^")
		return 1

	###Something to loop back on. Reminds me of those CS Grad memes. ;_;
	else:
		print("Okay, be serious here... %s is probably not a youtube link...") %fileinput
		startUp()

startUp()