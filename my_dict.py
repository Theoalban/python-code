#Dictionary {} Dictionaries in Python are a collection of key-value pairs. They are highly flexible and WIDELY used for data manipulation
d={'name':'Serge', 'age': 30, 'profession': 'DevOps Engineer', 'courses':['aws','linux','terraform']}

#Dict methods .clear(), .copy(), .get() items(), keys(), values(), pop(), popitem(), update(dict), del(dict[key])          
print(d.keys())
print(d.values())
print(d['courses'])
print(d.items())
 # iterates over all the keys in a dictionary d and prints each key along with its corresponding value, using f-string
for key, value in d.items():
    print(f"{key}: {value}") 

if  'name' in d:
    print('Name is present')
else:
    print("Name isn't present") 

    

