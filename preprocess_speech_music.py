"""
!!! To replicate this code you need sox to be installed in your system.
This program takes audio files in one directory and trims them using sox command to 25-30 second files, stored in another directory.
To run this run the command: 
python preprocess_speech_music.py <input_directory> <output_directory>
Eg: " python preprocess_speech_music.py ORG_DATA/TRAIN/MUSIC PROCESSED_DATA/TRAIN/MUSIC "
For this project, it is used for the train, test files of speech and music category.
"""

#Libraries
import argparse
import glob
import re
import os

#Setting the argument parser for input and output directory

parser = argparse.ArgumentParser(description='Directory names')
parser.add_argument('input', help='Input Directory Name for all the input files')
parser.add_argument('output', help='Output Directory Name for all the trimmed files')
args = parser.parse_args()

input_directoy=args.input
output_directory=args.output

for (i,file) in enumerate(glob.glob(input_directoy+"/*.wav")):
	filename=re.split(r'\.',re.split(r'\/',file)[-1])[0]
	if(i%6==0):
		os.system("sox "+ file +" " + output_directory+ "/" + filename + ".wav trim 0 25") #Using Sox command to trim the audio to only the first 25 secs
	elif(i%6==1):
		os.system("sox "+ file +" " + output_directory+ "/" + filename + ".wav trim 0 26") #Using Sox command to trim the audio to only the first 26 secs
	elif(i%6==2):
		os.system("sox "+ file +" " + output_directory+ "/" + filename + ".wav trim 0 27") #Using Sox command to trim the audio to only the first 27 secs
	elif(i%6==3):
		os.system("sox "+ file +" " + output_directory+ "/" + filename + ".wav trim 0 28") #Using Sox command to trim the audio to only the first 28 secs
	elif(i%6==4):
		os.system("sox "+ file +" " + output_directory+ "/" + filename + ".wav trim 0 29") #Using Sox command to trim the audio to only the first 29 secs	
	elif(i%6==5):
		os.system("sox "+ file +" " + output_directory+ "/" + filename + ".wav trim 0 30") #Using Sox command to trim the audio to only the first 30 secs


#Varying the duration to ensure there is variation in the data, so that the model is not just used to spectrogram features from audio files of duration 25 secs.