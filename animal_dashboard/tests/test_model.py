from models.animal_shelter import AnimalShelter

def test_read_returns_list():
    shelter = AnimalShelter()
    result = shelter.read()
    assert isinstance(result, list)
