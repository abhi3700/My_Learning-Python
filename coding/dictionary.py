import json		# To display dictionay with beautification

dic = dict(Dict1= {'1': dict(name= dict(first= 'Abhijit', last= 'Roy'), place= dict(city= 'coochbehar', state= 'West bengal')), '2': 'F'})

print("Nested dictionary:") 

# print(Dict) 
print(json.dumps(dic, indent= 2)) # Beautify dictionary using `json`

# get first name of person 1
print('Person 1\'s first name is: {0}'.format(dic['Dict1']['1']['name']['first']))