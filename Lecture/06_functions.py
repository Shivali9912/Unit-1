# %%
# Use def keyword to define a function
def greeting(name):
    print(f'Hi {name}, welcome to ACDA class!')

greeting('Shivali')

# %%

def add(a, b):
    return a + b


print(add(23, 12))

print(add('Hello', 'Bye'))

print(12, 'Bye')

# %%
def new_add(a: int, b: int):
    return a + b
print(new_add(12,45))
print(new_add(12,45.8))






# %%
# Use return keyword if the function has a return value.
def add(a, b):
    return a + b


print(add(23, 12))

print(add('Hello', 'Bye'))

print(12, 'Bye')

# %%
# Declare the type of data

def new_add(a: int, b: int):
    return a + b

print(new_add(12,45))
print(new_add(12,45.8))

# %%
# Casting the variables

a = 22
b  = '35'

print(str(a) + b)
print(a + int(b))