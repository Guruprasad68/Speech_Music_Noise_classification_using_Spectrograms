"""
This program takes audio files(noise) in one directory and concatenates/trims them using sox command to 25-30 second files, stored in another directory.
To run this run the command: 
python preprocess_noise.py <input_directory> <output_directory>
Eg: " python preprocess_noise.py ORG_DATA/TRAIN/MUSIC PROCESSED_DATA/TRAIN/MUSIC "
For this project, it is used for the train, test files of noise category.
"""

#Libraries
import argparse
import glob
import re
import os
import subprocess
import numpy as np

#Setting the argument parser for input and output directory

parser = argparse.ArgumentParser(description='Directory names')
parser.add_argument('input', help='Input Directory Name for all the input files')
parser.add_argument('output', help='Output Directory Name for all the trimmed files')
args = parser.parse_args()

input_directoy=args.input
output_directory=args.output


#Recursive function that concates the input noise file to itself until duration is greater than 25 secs
def merge_audio(input_file,output_directory,output_filename,i):
	cwd=os.getcwd()
	if(i==1):
		os.system("sox "+input_file+" " +input_file+" " + cwd+"/"+"temp1.wav")
	elif(i==2):
		os.system("sox "+cwd+"/"+"temp1.wav"+" " + input_file+" "+ cwd+"/"+"temp2.wav")
		os.system("cp temp2.wav temp1.wav")
		os.system("rm temp2.wav")
	
	cmd="soxi -D "+ cwd+"/"+"temp1.wav"
	duration=re.findall('\d*\.?\d+',str(subprocess.Popen( cmd,shell=True, stdout=subprocess.PIPE).stdout.read()))[0]
	if(float(duration)<25):
		merge_audio(input_file,output_directory,output_filename,2)
	
	return 1




for (i,file) in enumerate(glob.glob(input_directoy+"/*.wav")):
	random_duration=np.random.randint(25,31,size=1)[0]
	filename=re.split(r'\.',re.split(r'\/',file)[-1])[0]
	print(filename)
	cmd="soxi -D "+ file
	duration=re.findall('\d*\.?\d+',str(subprocess.Popen( cmd,shell=True, stdout=subprocess.PIPE).stdout.read()))[0]
	temp=0
	
	if(float(duration)>30): #If Noise duration is greater than 30 secs, we trim it to a randdom duration between 25 and 30 secs.
		os.system("sox "+ file +" " + output_directory+ "/" + filename + ".wav trim 0 "+str(random_duration))
	elif(float(duration)< 25): #Otherwise concate the noise to itslef until duration is greater than 25 secs using the recursive function
		temp=merge_audio(file,output_directory,filename,1)

	if(temp==1): #Just the cases when the recursive function is called
		cmd2="soxi -D temp1.wav"
		duration_temp2=re.findall('\d*\.?\d+',str(subprocess.Popen( cmd2,shell=True, stdout=subprocess.PIPE).stdout.read()))[0]
		if(float(duration_temp2)>30):
			os.system("sox temp1.wav" +" " + output_directory+ "/" + filename + ".wav trim 0 "+str(random_duration))
		else:
			os.system("cp temp1.wav "+output_directory+"/"+filename+".wav")
		
	
	if(float(duration)>=25 and float(duration)<=30): #If the file is already between 25 and 30 secs we just copy it to the output folder
		os.system("cp "+file+" "+output_directory+"/"+filename+".wav")

os.system("rm temp1.wav") #All processing done, so temp1.wav can be removed now