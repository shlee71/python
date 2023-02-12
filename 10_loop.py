names = ['shlee','sylee','jiryu']

for name in names:
    print('Hi, '+name+'. Bye, '+name+'.')

print('='*50)

persons = [
    ['egoing','Seoul','Web'],
    ['basta','Seoul','IOT'],
    ['blackjoe','Busan','ML']
]

print(persons[0][0])
for person in persons:
    print(person[0]+','+person[1]+','+person[2])

person = ['egoing','Seoul','Web']
name=person[0]
address=person[1]
job=person[2]
print(name,address,job)

print('='*50)
name, address, interest = ['egoing', 'Seoul', 'Web']
print(name, address, interest)
 
for name, address, interest in persons:
    print(name+','+address+','+interest)

print('='*50)

person = {'name':'egoing','city':'Seoul', 'job':'Web'}
print(person['name'])

for key in person:
    print(key, person[key])

print('='*50)


persons = [
    {'name':'egoing','city':'Seoul', 'job':'Web'},
    {'name':'basta','city':'Seoul', 'job':'IOT'},
    {'name':'blackjoe','city':'Busan', 'job':'ML'}
]

for person in persons:
    print(person)
print('='*50)
for person in persons:
    for key in person:
        print(key, person[key])
    print('-------------')
