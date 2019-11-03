# create a mapping of states to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# crete a basic set of states and cities in them
cities = {
    'CA': 'san fransico',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'PortLand'

#print out some cities
print('-' *15)
print("NY state has:", cities['NY'])
print("OR state has:", cities['OR'])

# print some states
print('-'*15)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# do it by using the state then cities dict
print('-'*15)
print('Michigan has:', cities[states['Michigan']])
print('Florida has:', cities[states['Florida']])

# print every state abbreviation
print('-'*15)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-'*15)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 15)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}") 

print('-' * 15)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
        print("sorry, no Texas.")
        
#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

