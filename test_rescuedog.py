from rescuedog import *

doglist = [['jake',8,'terrier',['untrimmed','unhealthy','hungry']]]
def test_dog_class():
    dog = Dog(doglist[0][0],doglist[0][1],doglist[0][2],doglist[0][3])
    assert dog.name == 'jake'
    assert dog.age == 8
    assert dog.breed == 'terrier'
    assert dog.condition == ['untrimmed','unhealthy','hungry']
    dog.groom()
    assert 'untrimmed' not in dog.condition
    assert 'unhealthy' in dog.condition and 'hungry' in dog.condition
    dog.heal()
    assert 'unhealthy' not in dog.condition
    dog.feed()
    assert 'hungry' not in dog.condition
def test_Main_Handler_class():
    dog1 = Dog('jake',8,'terrier',['untrimmed','unhealthy','hungry'])
    dog2 = Dog('punjab',38,'dane',['untrimmed','unhealthy','hungry'])
    doglist = [dog1,dog2]
    vet = Vet()
    trainer = Trainer()
    groomer = Groomer()
    main_handler = Main_Handler(doglist,[vet],[groomer],[trainer])
    assert main_handler.dog_count() == 2
    assert main_handler.vet_count() == 1
    assert main_handler.groom_count() == 1
    assert main_handler.train_count() == 1