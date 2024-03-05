#Alex Ferguson
#3/4/24
#Dictionaries can be used to map keys to values

capitals = {'USA': 'Washington D.C.',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#Clears only China value
capitals.clear()
#Clears entire dictionary

#print(capitals['Germany'])
# Errors out
print(capitals.get('Germany'))
#Returns none 
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#Prints all the values and keys

for key, value in capitals.items():
    print(key,value)
#Prints entire dictionary

