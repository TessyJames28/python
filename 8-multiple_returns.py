#!/usr/bin/python3

# Function that returns a tuple with the length of a string and its first character.

def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        return (len(sentence), sentence[0]) 
    

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))