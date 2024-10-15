# %%
# List

cars= ['Honda' , 'Ford', 'Tesla' , 'BMW' , 'GMC']

# %%
# Use the len() method to return the length of a list
print(f'Number of cars:{len(cars)}')

# %%

# Operations over list
values = [5 , 4,-4, 8, 8.9 , -2.5, 12, 7.8 ]
print(len(values))
print(max(values))
print(min(values))
print(sum(values))

# %%
# Refer to a list element by referring to the index number (0-based)
print(f'First car is {cars[0]}')
print(f'Last car is {cars[4]}')

print(f'Last car is {cars[len(cars)-1]}')
print(f'Last car is {cars[-1]}')
print(f'Second last car is {cars[-2]}')

# %%
# List Comprehension
terms = 'Advanced Concepts in Data Analytics'
# %%
# Example 1 - get all letters in a string and store them in a list
all_letters = []
for letter in terms:
    all_letters.append(letter)
print(all_letters)

# %%
# A more Pythonic way to achieve this task is as follow.

all_letters= [letter for letter in terms]
print(all_letters)

# %%

# Example 2 - get all non-vowel letters in a string and store in a list

vowels= 'aeiou'
non_vowels_letters = [letter for letter in terms.lower() if letter not in vowels]
print (non_vowels_letters)

