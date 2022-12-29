# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} : {v}')

# dictionary unpacking
d= {'name':'Uttam', 'age':24}
func(**d)
