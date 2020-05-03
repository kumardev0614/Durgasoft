# Here we will learn what is:
# Class
# Object
# Reference variable

# Suppose We have to built Many TV sets of new model
# Then there will be a design of that TVs with there internal architecture, properties, Things that TV can do etc
# 1) Class = This DESIGN will work as ClASS

# Now based on the design We will create n number of TVs
# 2) Object = Those actual manufactured TVs are nothing but object of the class.

# And we know to do any task with TV we need it's remote.
# 3) Reference Variable = So here remote works as Reference variable


class TV:
    '''This is documentation String for TV class.
This TV is designed By Our main Technology Head Mr. DK Bharti '''

    def __init__(self, id):
        self.color = 'black'
        self.volume = 15
        self.id = id

    def volumeUp(self):
        self.volume = self.volume + 1

    def volumeDown(self):
        self.volume = self.volume - 1

    def showProperties(self):
        print("TV's properties are:")
        print('Id =',self.id)
        print('Color =',self.color)
        print('Volume =',self.volume)



print(TV.__doc__)

print()
remote1 = TV(1515)      # Creating TV object and its Reference variable
print('By Default TV 1515 volume =',remote1.volume)
remote1.volumeUp()
remote1.volumeUp()
remote1.volumeUp()
remote1.volumeUp()
print('After increasing volume by remote, volume =', remote1.volume)
remote1.showProperties()

print()
remote2 = TV(1516)
print('By Default TV 1516 volume =', remote2.volume)
remote2.volumeDown()
remote2.volumeDown()
remote2.volumeDown()
remote2.volumeDown()
remote2.volumeDown()
print('After Decreasing volume by remote, volume =', remote2.volume)
remote2.showProperties()

help(TV)