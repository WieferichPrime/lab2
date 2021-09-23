from simple import simple
from Person import Person
import random

n = int(input('Введите положительное число n: '))
simpleNumbs = simple(n)
p = random.randint(2, 1000)
q = random.randint(2, 1000)

rand = random.randint(0, len(simpleNumbs) - 1)
alice = Person(rand, q, p)

rand = random.randint(0, len(simpleNumbs) - 1)
bob = Person(rand, q, p)

alice.say(bob)
bob.say(alice)

print('Алиса передаёт',alice.said, 'Бобу')
print('Боб передаёт' , bob.said, 'Алисе')
print('q = ',q)
print('p = ',p)
print('a = ',alice.a)
print('b = ',bob.a)

aliceKey = bob.listened ** bob.a % p
if alice.listened ** alice.a % p == aliceKey:
    print('Ключ:', aliceKey)