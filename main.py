from simple import simple
from Person import Person
import random

n = int(input('Введите положительное число n: '))
simpleNumbs = simple(n)
p = random.randint(2, 1000)
q = random.randint(2, 1000)
rand = random.randint(0, len(simpleNumbs) - 1)
while not simpleNumbs[rand]:
    rand = random.randint(0, len(simpleNumbs) - 1)
rand1 = random.randint(0, len(simpleNumbs) - 1)
while not simpleNumbs[rand1]:
    rand1 = random.randint(0, len(simpleNumbs) - 1)

alice = Person(rand, q, p)
bob = Person(rand1, q, p)

alice.say(bob)
bob.say(alice)

print('Алиса передаёт',alice.said, 'Бобу')
print('Боб передаёт' , bob.said, 'Алисе')
print('q = ',q)
print('p = ',p)
print('a = ',rand)
print('b = ',rand1)

aliceKey = bob.listened ** rand1 % p
if alice.listened ** rand % p == aliceKey:
    print('Ключ:', aliceKey)