class Person:
    def __init__(self, a=2, q=0, p=0):
        self.a = a
        self.q = q
        self.p = p
        self.said = ''
        self.listened = ''

    def say(self, person):
        self.said = (self.q ** self.a) % self.p
        person.listened = self.said

