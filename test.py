def replace_ending(sentence, old, new):
	if old in sentence :
		i = sentence.split(" ")
		new_sentence = " ".join(i[:len(i)-1])+" "+new
		return new_sentence
	# Return the original sentence if there is no match 
	return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

print()