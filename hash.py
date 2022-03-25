import os
import hashlib
import time
from difflib import Differ

rootdir = "/home/sy402/Desktop/"
avoidDir = ["dev",'proc','run', 'sys', 'tmp', 'var',"notDir"]

def printer():
	for dirpath, dirnames, filenames in os.walk(rootdir):
		dirnames[:] = [dirname for dirname in dirnames if dirname not in avoidDir]
		for i in filenames:
			filePath = os.path.join(dirpath,i)
			print(filePath)

def option2():
	writeList = []

	for dirpath, dirnames, filenames in os.walk(rootdir):
		dirnames[:] = [dirname for dirname in dirnames if dirname not in avoidDir]
		for i in filenames:
			filePath = os.path.join(dirpath,i)

			try:
				with open(filePath,"rb") as f:
					bytes = f.read()
			except (FileNotFoundError, PermissionError):
				continue
			else:
				timestr = time.strftime("%Y%m%d-%H%M%S")
				appender = filePath + " | " + (hashlib.sha256(bytes).hexdigest())+ " | " + timestr
				writeList.append(appender)
	timestrFile = time.strftime("%Y%m%d-%H%M%S")
	writeFilePath = "/home/sy402/Desktop/"
	conCat = writeFilePath + timestrFile + ".txt"
	with open(conCat,"w") as writeFile:
		for x in writeList:
			writeFile.write(x)
			writeFile.write("\n")

def difference1(file1,file2):
	print(file1)
	print(file2)
	print("Summary:")
	with open (file1,'r') as filex, open (file2, 'r') as filey:
		differ = Differ()

		for line in differ.compare(filex.readlines(), filey.readlines()):
			print(line)

def main():
	print("Welcome to TripWYRE.\n\nYour options are:\n1: Run TripWYRE on system.\n2: Compare two files for system integrity.\n3: Print all files in system.\n")
	x = input("\nPlease select your option.\n")
	if x == "1":
		option2()
		print("Complete! Check desktop for output file.")
	elif x == "2":
		q = input("Please type the name of the original TripWYRE file.\n")
		w = input("Please type the name of the secondary TripWyre file.\n")
		difference1(q,w)
	elif x == "3":
		printer()
	else:
		print("Invalid Input. Quitting now.")

main()
