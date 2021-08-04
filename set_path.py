__author__ = 'Sudhir'
__date__ = "Aug 3 - 2021"

'''
Purpose : To set the package search path for user defined packages.
'''

import sys
import os

path = os.getcwd()
for folder in os.listdir(path):
	if(os.path.isdir(folder) and folder not in ['.git', 'Database']):
		sys.path.append('./'+folder)