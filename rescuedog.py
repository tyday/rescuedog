import asyncio
import time
from datetime import datetime

async def custom_sleep(x):
    print('Sleep', datetime.now())
    await asyncio.sleep(x)
async def empty_space():
    print('this is empty. A waste of time.')

# Dog Object that holds a dog
# includes name, age, breed
# the last element was state... but I think I'm going to include multiples
# hair: trimmed/untrimmed
# health: healthy/unhealthy
# hunger: fed/hungry
# or condition = ['untrimmed','unhealthy','hungry'] then... either remove conditions or replace them with trimmed,healthy,fed
# a dog that is trimmed, healthy and hungry is either ready for sale? or moved from the Pen
class Dog:
    def __init__(self,name,age,breed,condition=['untrimmed','unhealthy','hungry']):
        self.name = name
        self.age = age
        self.breed = breed
        self.condition = condition

    def groom(self):
        if 'untrimmed' in self.condition:
            self.condition.remove('untrimmed')
    
    def heal(self):
        if 'unhealthy' in self.condition:
            self.condition.remove('unhealthy')
        
    def feed(self):
        if 'hungry' in self.condition:
            self.condition.remove('hungry')
# A Pen
# holds dogs
# It can either be a list object that holds the dogs or
# it can be something more interesting that calls the controller object to alert them of incoming dogs
# does the pen work autonomously from the controller? or does the controller field new dogs and pen them?

# Vet - heals the dog
class Vet:
    population = 0

    def __init__(self):
        Vet.population += 1
        self.name = "Vet #" + str(Vet.population)
        print('Acquireing {}'.format(self.name))
    
    async def treat_dog(self,dog):
        if 'unhealthy' in dog.condition:
            dog.heal()
            await custom_sleep(2)

# groomer - grooms dog
class Groomer:
    population = 0
    def __init__(self):
        Groomer.population += 1
        self.name = "Groomer #" + str(Groomer.population)
    async def groom_dog(self, dog):
        if 'untrimmed' in dog.condition:
            dog.groom()
            await custom_sleep(2)

# trainer - feeds dog
class Trainer:
    population = 0
    def __init__(self):
        Trainer.population += 1
        self.name = "Trainer #" + str(Trainer.population)
    async def feed_dog(self, dog):
        if 'hungry' in dog.condition:
            dog.feed()
            await custom_sleep(2)

# Handler - handles the main loop
class Main_Handler:
    def __init__(self, dogqueue, veterinarians, groomers, trainers):
        self.dogqueue = dogqueue
        self.veterinarians = veterinarians
        self.groomers = groomers
        self.trainers = trainers
    def dog_count(self):
        x = len(self.dogqueue)
        return x
    def vet_count(self):
        return len(self.veterinarians)
    def groom_count(self):
        return len(self.groomers)
    def train_count(self):
        return len(self.trainers)
if __name__ == "__main__":
    doglist = [['jake',8,'terrier',['untrimmed','unhealthy','hungry']]]
    for animal in doglist:
        start_time = datetime.now()
        dog = Dog(doglist[0][0],doglist[0][1],doglist[0][2],doglist[0][3])
        print(dog.name, dog.condition)
        vet = Vet()
        groomer = Groomer()
        trainer = Trainer()
        loop = asyncio.get_event_loop()
        tasks = [vet.treat_dog(dog),empty_space(),groomer.groom_dog(dog),trainer.feed_dog(dog)]
        # vet.treat_dog(dog)
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        print(dog.name,dog.condition)
        finish_time = datetime.now()
        print(finish_time-start_time)