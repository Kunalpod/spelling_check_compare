import jellyfish
import editdistance
import json
import pickle
from collections import defaultdict


def load_valid_words():
	words = []
	with open("../EnWords","rb") as f:
		words = pickle.load(f)
	words = [x.strip() for x in words]	
	return words
global valid_words
valid_words = load_valid_words()
print("Loaded valid words")

def load_misspelled_words():
	dict = {}
	with open("missp.json") as f:
		dict = json.load(f)
	return dict	
global misspelled_words
misspelled_words = load_misspelled_words()
print("Loaded mispelled dataset")

def phonetic(word):
	return jellyfish.metaphone(word)


def how_close1(str1, str2):
	return jellyfish.levenshtein_distance(phonetic(str1), phonetic(str2))


def levenshtein_key(word):
	return editdistance.eval(word[0],word[1])


def main():
	correct = 0
	total = 0
	for key in misspelled_words:
		print("\t",key)
		for word in misspelled_words[key]:
			total += 1
			alternatives = [[word, w] for w in valid_words if how_close1(w, word) <3]
			alternatives = sorted(alternatives, key = levenshtein_key)
			alternatives = [x[1] for x in alternatives]
			if key in alternatives[:10]:
				correct += 1

		if(total >= 50000): break
	print("Correct : ", correct)	
	print("Total : ", total)

main()