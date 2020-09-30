class Bird:
    def __init__(self, name, age, variety):
        self.name = name
        self.age = age
        self.variery = variety
    

class Pets:
    def __init__(self, birds):
        self.birds = birds
        
        
bird1 = Bird("Tweety", 6, "canary")
bird2 = Bird("BeepBeep", 7, "road runner")
bird3 = Bird("Iago", 9, "parrot")
inputBirds = [bird1, bird2, bird3]
pets = Pets(inputBirds)

print("I have "+ str(len(pets.birds))+" pets:")
for bird in pets.birds:
    print(bird.name + ", a " + bird.variery + " is " +str(bird.age))

