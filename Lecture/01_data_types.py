# Data Types


# %%

a = "Hello"
b = 45
c = 12.36
d = 2+5j #complex(2, 5)
e = True
f = "123" #str(123)


print(f'a={a}, b={b}, c={c}, d={d}, e={e}')


# %%
# Sequence types


a_list = [2, 3, 2 ,5, 4, 3] #list
b_list = [5, -7, 9, 'd', '123'] #list
c_set = {2, 3, 4, 5, 3, 5, 3} #set}
d_tuple = (2, 5, 2, 'a')
e_frozen_set = frozenset(c_set)
f_range = range(5)

print(f'a_list={a_list}, \nb_list={b_list}, \nc_set={c_set}, \nd_tuple={d_tuple}, \ne_frozen_set={e_frozen_set}, \nf_range={f_range}')

# %%
# Mapping Type: dict
a = {1:"good", 2:"Not good"}
print(f'{a}')


# %%
