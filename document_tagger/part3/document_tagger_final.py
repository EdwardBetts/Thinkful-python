import re
import sys
import os

title_search = re.compile(r'(?:title:\s*)(?P<title>(.*)[ ]*?\n[ ]*(.*))', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)


def file_path(directory, file_name): 
	return os.path.join(directory,file_name)

def file_read(fl_path): 
	with open(fl_path, 'r') as f:
		return f.read()

def kw_pattern(kws)
	result = {kw: re.compile(r'\b' + kw + r'\b') for kw in kws}
	return result

def kw_counter(pattern, text):
	matches = re.findall(pattern,text)
	return len(matches)

'''
import os
dirs = os.listdir(".")
for dir in dirs:
    new_dirs = os.listdir(os.path.join(".", dir))
    "." + "/" + dir
'''
