states = {
    'Haryana': 'HR',
    'Punjab': 'PB',
    'Rajasthan': 'RS',
    'Uttarpradesh': 'UP'
}
cities = {
    'HR': 'faridabad',
    'PB': 'ludhiyana',
    'RS': 'jaisalmer'
}
cities['UP'] = 'bulandsheher'

# print some states
print('*' * 25)
print("Haryana's abbreviation is ",states['Haryana'])
print("Punjab's abbreviation is ",states['Punjab'])

# do it with some cities
print('*' * 25)
print("Haryana has:", cities[states['Haryana']])
print("Punjab has:", cities[states['Punjab']])

#printing every city in state
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 25)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
