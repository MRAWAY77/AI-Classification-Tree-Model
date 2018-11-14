import numpy as np
import os 
import math
import pandas as pd
import csv
import glob
import shutil

Gender = ['male','female']
Class = ['Pclass1','Pclass2','Pclass3']
Price = ['Low_Fare','Middle_Fare','High_Fare']
Maturity = ['Young','Adult','Senior','Elderly','Unknown']
Number = ['Alpha','Digit']
Place = ['S','C','Q','U']
Position = ['CabinA','CabinB','CabinC','CabinD','CabinE','CabinF','CabinG','Missing'] 
Siblings = [0,1,2,3,4,5]
ParCH = [0,1,2,3,4,5]

def remove(filelist):
	for j in filelist:
		with open(j) as infocsv:
		    reader = [i for i in csv.DictReader(infocsv)]
		    if len(reader)>0:
		        print ('not empty')
		    else:
		        print ('empty')
		        os.remove(j)

def move(src,dst):
	for i in src:
		shutil.move(i, dst)

name = glob.glob('/home/alvinwong/Desktop/AI/Validation/*.csv')

remove(name)