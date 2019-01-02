""" 
Python script to implement an Interactive Dictionary
		by Aniruddha
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json")) #default file mode is r

def meaning(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	else:
		similar_word = get_close_matches(word,data.keys(),1,0.8)
		if len(similar_word) > 0:
			response = ''
			while response not in ('Y','y','N','n'):
				response = input("[?] Did you mean %s instead? (y/n) : " %similar_word[0])
			if response in ['Y','y']:
				return data[similar_word[0]]
			
	return "Word doesn't exist.Please double check it"



print("This is a Dictionary written in python by Aniruddha")
while True:
	word = input("\n==>Enter word (Empty input to quit) : ")
	if word != '':
		output = (meaning(word))

		if type(output) == list:
			for item in output:
				print("[*] ",item)
		else:
			print("[!] ",output)
	else:
		break

print("\nThanks for using my dictionary.Good Bye!...")
	
	


#Sample Output:
#	This is a Dictionary written in python by Aniruddha

#	==>Enter word (Empty input to quit) : rain
#	[*]  Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.
#	[*]  To fall from the clouds in drops of water.

#	==>Enter word (Empty input to quit) : RaIn
#	[*]  Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.
#	[*]  To fall from the clouds in drops of water.

#	==>Enter word (Empty input to quit) : delhi
#	[*]  The largest metropolis by area and the second-largest metropolis by population in India.

#	==>Enter word (Empty input to quit) : DELHI
#	[*]  The largest metropolis by area and the second-largest metropolis by population in India.

#	==>Enter word (Empty input to quit) : usa
#	[*]  A country and federal republic in North America located north of Mexico and south of Canada, including Alaska, Hawaii and overseas territories.

#	==>Enter word (Empty input to quit) : Rainn
#	[?] Did you mean rain instead? (y/n) : y
#	[*]  Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.
#	[*]  To fall from the clouds in drops of water.

#	==>Enter word (Empty input to quit) : Rainn
#	[?] Did you mean rain instead? (y/n) : n
#	[!]  Word doesn't exist.Please double check it

#	==>Enter word (Empty input to quit) : Rainn
#	[?] Did you mean rain instead? (y/n) : a
#	[?] Did you mean rain instead? (y/n) : abcd1234
#	[?] Did you mean rain instead? (y/n) : y
#	[*]  Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.
#	[*]  To fall from the clouds in drops of water.

#	==>Enter word (Empty input to quit) : 

#	Thanks for using my dictionary.Good Bye!...


