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
def test_Clinic_class():
    # dog1 = Dog('jake',8,'terrier',['untrimmed','unhealthy','hungry'])
    # dog2 = Dog('punjab',38,'dane',['untrimmed','unhealthy','hungry'])
    # doglist = [dog1,dog2]
    # vet = Vet()
    # trainer = Trainer()
    # groomer = Groomer()
    clinic = Clinic()
    clinic.generate_clinic(5,2,2,2,2)
    assert clinic.dog_count_entry() == 5
    assert clinic.vet_count() == 2
    assert clinic.groom_count() == 2
    assert clinic.train_count() == 2
    assert clinic.valet_count() == 2
    valet = clinic.valets[0]
    i = clinic.dog_count_entry()
    for dog in clinic.entry_queue[:]:
        valet.enter_dog(dog,clinic)
        i -= 1
        assert clinic.dog_count_entry() == i
    assert clinic.dog_count_pen() == 5