#level1-grandparent = animal
#level2-parent = cat, dog, mouse
#level3-child = siamese, jack russel, mickey
input_what_animal = input("Are you interested in adopting a dog, a cat, or a mouse?")

class Animal():

    def __init__(self, name, what_animal, pref_activity, age=0): #level1-grandparent = animal
        self.name = name
        self.what_animal = what_animal
        self.pref_activity = pref_activity
        self.age = age
    
    def who_am_i(self):
        print(Atticus)
    
    def fetch(self, throws):
        throws = int(input("How many times will you throw the ball for me?\n"))
        throw_counter = 0
        while throw_counter <= (throws - 1):
            print("I fetch, woof, I fetch, I'm on it, Yay! Fetch! Play with me! I love you!")
            throw_counter += 1   
   
    def __str__(self):
        return (self.name + self.what_animal + self.pref_activity + str(self.age))

Atticus = Animal("Atticus\n", "Dog\n", "Fetch!\n", 9)    
Atticus.who_am_i()
Atticus.fetch(0)