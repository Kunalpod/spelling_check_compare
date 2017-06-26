import json
import re
import pickle

def load_valid_words():
	words = []
	with open("../EnWords","rb") as f:
		words = pickle.load(f)
	words = [x.strip() for x in words]	
	return words
global valid_words
valid_words = load_valid_words()

def json_dict(dict):
	with open('missp.json', "w") as f:
		json.dump(dict, f, indent = 4)
	print("Saved")

dict = {}
with open("missp.txt") as f:
	for line in f:
		if line[0] == '$':
			key = line[1:].strip().lower()
			if '-' in key or '_' in key or key not in valid_words:
				key = ""	
		elif key!="":
			if key in dict:	dict[key].append(''.join(x for x in line.strip().lower() if re.match("[a-z]", x)))
			else: dict[key] = [''.join(x for x in line.strip().lower() if re.match("[a-z]", x))]
	f.close()		
json_dict(dict)