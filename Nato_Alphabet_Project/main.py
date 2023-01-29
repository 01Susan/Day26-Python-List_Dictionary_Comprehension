import pandas as pd

# TODO 1. Create a dictionary in this format:

data = pd.read_csv("nato_phonetic_alphabet.csv")
# Creating a new dictionary using data -->Dataframe
# using the dictionary comprehension
code_letter = {rows.letter: rows.code for (index, rows) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter you name : ").upper()
# Using the list comprehension
name_list = [code_letter[letter] for letter in word]
print(name_list)
