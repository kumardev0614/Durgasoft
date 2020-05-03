# Nested classes are example of Inner Classes concepts.
# Here we will go up to 3 levels Human-> Head-> Brain


class Human:
    def __init__(self, name, hair, iq):
        self.name = name
        self.HEAD = self.Head(hair, iq) # we have created object type variable HEAD,To access Head class by Human class

    def display(self):
        print(self.name)
        print(self.HEAD.hair)
        print(self.HEAD.BRAIN.iq)

    class Head:
        def __init__(self, hair, iq):
            self.hair = hair
            self.BRAIN = self.Brain(iq) # we have created object type variable BRAIN,To access Brain class by Head class

        def talk(self, words):
            print('Saying:',words)

        class Brain:
            def __init__(self, iq):
                self.iq = iq

            def think(self, idea):
                print('Thinking on', idea)


h = Human('Dev', 'long', 150)
print(h.name)
h.HEAD.talk('hello')
print(h.HEAD.hair)
h.HEAD.BRAIN.think('sports')
print(h.HEAD.BRAIN.iq)

print('---------------------')
h2 = Human('Raj', 'Short', 50)
print(h2.name)
h2.HEAD.talk('good morning')
print(h2.HEAD.hair)
h2.HEAD.BRAIN.think('books')
print(h2.HEAD.BRAIN.iq)

print('----------------------')
h3 = Human('luv', 'red', 55)
h3.display()

