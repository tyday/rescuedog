import asyncio
import time, random
from datetime import datetime

async def custom_sleep(x):
    # print('Sleep', datetime.now())
    await asyncio.sleep(x)
async def empty_space():
    print('this is empty. A waste of time.')
conditions_descriptions = {'unhealthy':'healing','untrimmed':'grooming','hungry':'feeding'}
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
    def __repr__(self):
        # return {'name:':self.name, 'age:':self.age, 'breed:':self.breed,'cond:':self.condition}
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}, Cond:{self.condition}"

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

class employee:
    async def routine(self,clinic):
        cycle = 1

        while clinic.running:
            sleep_time = 0
            try: #if self.repair in clinic.conditions['unhealthy']:
                if clinic.conditions[self.repair] > 0:
                    dog = clinic.get_dog(self.repair)
                    clinic.rem_dog_pen(dog)
                    print(f'{self.name} is {conditions_descriptions[self.repair]} {dog.name}')
                    await custom_sleep(self.repair_time)
                    if self.repair in dog.condition:
                        dog.condition.remove(self.repair)
                    clinic.add_dog_pen(dog)
                else:
                    cycle += 1
                    if cycle > 10:
                        sleep_time = cycle//10
                    elif cycle > 100:
                        sleep_time = 10
                    else:
                        sleep_time = 1
                    if cycle%10 == 0:
                        print(f'{self.name} sleeping for {sleep_time} seconds.')
                    await custom_sleep(sleep_time)
            except:
                print(f'An exception occured for {self.name}.')
                await custom_sleep(1)

# Vet - heals the dog
class Vet(employee):
    population = 0

    def __init__(self):
        Vet.population += 1
        self.name = "Vet #" + str(Vet.population)
        self.repair = 'unhealthy'
        self.repair_time = 10
        print('Acquireing {}'.format(self.name))
    def __repr__(self):
        return self.name    
    async def treat_dog(self,dog):
        if 'unhealthy' in dog.condition:
            dog.heal()
            await custom_sleep(2)

# groomer - grooms dog
class Groomer(employee):
    population = 0
    def __init__(self):
        Groomer.population += 1
        self.name = "Groomer #" + str(Groomer.population)
        self.repair = 'untrimmed'
        self.repair_time = 2
    def __repr__(self):
        return self.name
    async def groom_dog(self, dog):
        if 'untrimmed' in dog.condition:
            dog.groom()
            await custom_sleep(2)

# trainer - feeds dog
class Trainer(employee):
    population = 0
    def __init__(self):
        Trainer.population += 1
        self.name = "Trainer #" + str(Trainer.population)
        self.repair = 'hungry'
        self.repair_time = 2
    def __repr__(self):
        return self.name
    async def feed_dog(self, dog):
        if 'hungry' in dog.condition:
            dog.feed()
            await custom_sleep(2)

class Valet:
    population = 0
    def __init__(self):
        Valet.population += 1
        self.name = "Valet #" + str(Valet.population)
    def __repr__(self):
        return self.name
    async def enter_dog(self,dog,clinic):
        await custom_sleep(1)
        # clinic.rem_dog_entry(dog)
        clinic.add_dog_pen(dog)
    def exit_dog(self,dog,clinic):
        # await custom_sleep(1)
        clinic.rem_dog_pen(dog)
        clinic.add_dog_exit(dog)
    async def routine(self,clinic):
        cycle = 0
        while len(clinic.entry_queue) > 0:
            if len(clinic.entry_queue)>0:
                dog = clinic.entry_queue.pop()
                await self.enter_dog(dog,clinic)
                print(f'{self.name} transporting {dog.name} to pen.')
            else:
                cycle += 1
                if cycle > 10:
                    print(f'{self.name} sleeping.')
                    await custom_sleep(cycle//10)
                if cycle > 100:
                    print(f'{self.name} sleeping.')
                    await custom_sleep(10)
                else:
                    print(f'{self.name} sleeping.')
                    await custom_sleep(1)
''' clinic class will hold the employees and the animals
 entry_queue simulates the clinic waiting room. Dogs are brought in and sent to the pen
 the employees gather them from the pen and return them when finished
 the dog_return_que simulates dogs that have been returned'''
class Clinic:
    def __init__(self, dogqueue=[], veterinarians=[], groomers=[], trainers=[], valets=[]):
        self.entry_queue = dogqueue
        self.pen = []
        self.exit_queue = []
        self.veterinarians = veterinarians
        self.groomers = groomers
        self.trainers = trainers
        self.valets = valets
        self.running = True
        
        self.conditions = {}
    def generate_clinic(self,no_dogs,no_vets,no_groomers,no_trainers,no_valets):
        ''' This will setup the main handler with animals and employees'''
        breeds = ['Retriever','Terrier','Dane','Mutt','Poodle','Bulldog','Wolf','Sheepdog']
        for i in range(no_dogs):
            name = 'Dog #' + str(i+1)
            age = int((random.randint(1,15) + random.randint(1,15))/2)
            condition = ['untrimmed','unhealthy','hungry']
            breed = random.choice(breeds)
            dog = Dog(name,age,breed,condition)
            self.entry_queue.append(dog)
        for i in range(no_vets):
            vet = Vet()
            self.veterinarians.append(vet)
        for i in range(no_groomers):
            groomer = Groomer()
            self.groomers.append(groomer)
        for i in range(no_trainers):
            trainer = Trainer()
            self.trainers.append(trainer)
        for i in range(no_valets):
            valet = Valet()
            self.valets.append(valet)
    def add_dog_pen(self, dog):
        if len(dog.condition) == 0:
            dog.condition.append('Ready for home')
        for cond in dog.condition:
            if cond in self.conditions:
                self.conditions[cond] += 1
            else:
                self.conditions[cond] = 1
        self.pen.append(dog)
    def rem_dog_pen(self, dog):
        for cond in dog.condition:
            if cond in self.conditions:
                self.conditions[cond] -= 1
            else:
                print('error in rem_dog_pen')
        self.pen.remove(dog)
    def rem_dog_entry(self, dog):
        self.entry_queue.remove(dog)
    def add_dog_entry(self,dog):
        self.entry_queue.append(dog)
    def add_dog_exit(self,dog):
        self.exit_queue.append(dog)
    def rem_dog_exit(self,dog):
        self.exit_queue.remove(dog)
    def get_dog(self,condition):
        for dog in self.pen:
            if condition in dog.condition:
                return dog
        print(f'get_dog failed to find a dog with the condition: {condition}')
    def dog_count_entry(self):
        x = len(self.entry_queue)
        return x
    def dog_count_pen(self):
        x = len(self.pen)
        return x
    def vet_count(self):
        return len(self.veterinarians)
    def groom_count(self):
        return len(self.groomers)
    def train_count(self):
        return len(self.trainers)
    def valet_count(self):
        return len(self.valets)
    
    async def routine(self):
        try:
            while self.running:
                print(f"{clinic.conditions}")
                print(f"Dogs Entry: {len(clinic.entry_queue)} Dogs Pen: {len(clinic.pen)} Dogs Exit: {len(clinic.exit_queue)}")
                await custom_sleep(10)
        except:
            print('Error in clinic.routine()')
if __name__ == "__main__":
    # doglist = [['jake',8,'terrier',['untrimmed','unhealthy','hungry']]]
    # for animal in doglist:
    #     start_time = datetime.now()
    #     dog = Dog(doglist[0][0],doglist[0][1],doglist[0][2],doglist[0][3])
    #     print(dog.name, dog.condition)
    #     vet = Vet()
    #     groomer = Groomer()
    #     trainer = Trainer()
    #     loop = asyncio.get_event_loop()
    #     tasks = [vet.treat_dog(dog),empty_space(),groomer.groom_dog(dog),trainer.feed_dog(dog)]
    #     # vet.treat_dog(dog)
    #     loop.run_until_complete(asyncio.wait(tasks))
    #     loop.close()
    #     print(dog.name,dog.condition)
    #     finish_time = datetime.now()
    #     print(finish_time-start_time)
    clinic = Clinic()
    clinic.generate_clinic(5,2,2,2,2)
    print(clinic.dog_count_entry(), clinic.entry_queue)
    print(clinic.vet_count(), clinic.veterinarians)
    print(clinic.groom_count(),clinic.groomers)
    print(clinic.train_count(),clinic.trainers)
    print(clinic.valet_count(),clinic.valets)
    # for dog in clinic.entry_queue[:]:
    #     valet = clinic.valets[0]
    #     valet.enter_dog(dog,clinic)

    # for groomer in clinic.groomers:
    #     print(groomer)
    # for vet in clinic.veterinarians:
    #     print(vet)
    # for valet in clinic.valets:
    #     print(valet)
    # for dog in clinic.entry_queue[:]:

        
        
    print("entry queue",clinic.dog_count_entry(),clinic.entry_queue)
    print('Pen: ', clinic.pen)
    print(clinic.conditions)
    print("moving dogs...")
    loop = asyncio.get_event_loop()
    tasks = []
    employees = []
    for valet in clinic.valets:
        tasks.append(valet.routine(clinic))
    for vet in clinic.veterinarians:
        tasks.append(vet.routine(clinic))
    for groomer in clinic.groomers:
        tasks.append(groomer.routine(clinic))
    for trainer in clinic.trainers:
        tasks.append(trainer.routine(clinic))
    tasks.append(clinic.routine())
        # employees.append(trainer)
    # tasks = [employees[0].routine()]
    # vet.treat_dog(dog)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    # for dog in clinic.pen[:]:
    #     valet.exit_dog(dog,clinic)
    #     # clinic.rem_dog_pen(dog)
    print('Pen: ',clinic.pen)
    print(clinic.conditions)
    word='unhealthy'
    print(clinic.conditions[word],'--test')