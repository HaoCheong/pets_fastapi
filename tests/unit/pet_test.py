from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_create_pet(reset_db, pets_data):
    assert wrappers.create_pet(pets_data[0])['status'] == SUCCESS

def test_get_all_pet(reset_db, pets_data):
    pets = [wrappers.create_pet(pets_data[i])
                for i in range(0, len(pets_data))]

    for pet in pets:
        assert pet["status"] == SUCCESS

    all_pets = wrappers.get_all_pets()['data']
    assert len(pets) == len(all_pets)

def test_get_pet_by_pet_id(reset_db, pets_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    ret_pet = wrappers.get_pet_by_pet_id(pet['id'])['data']
    assert pet["name"] == ret_pet["name"]

def test_invalid_get_pet_by_pet_id(reset_db, pets_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    ret_pet = wrappers.get_pet_by_pet_id(pet['id'] + 200)
    assert ret_pet['status'] == ERROR

def test_delete_pet_by_pet_id(reset_db, pets_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    
    # Check pre-delete statue
    pre_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_pet_by_pet_id(pet['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_pet_by_pet_id(reset_db, pets_data):
    pet = wrappers.create_pet(pets_data[0])['data']

    # Check pre-delete statue
    pre_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_pet_by_pet_id(pet['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert post_check_res['status'] == SUCCESS

def test_update_pet_by_pet_id(reset_db, pets_data):

    # Checks that both pets data are identical
    pet = wrappers.create_pet(pets_data[0])['data']
    new_pet = pets_data[1]
    assert pet['name'] != new_pet['name']

    new_pet = pets_data[1]
    update_pet = wrappers.update_pet_by_pet_id(pet['id'], new_pet)
    assert update_pet['status'] == SUCCESS

    assert update_pet['data']['name'] == new_pet['name']

def test_invalid_update_pet_by_pet_id(reset_db, pets_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    new_pet = pets_data[1]
    update_pet = wrappers.update_pet_by_pet_id(pet['id'] + 200, new_pet)

    assert update_pet['status'] == ERROR

    post_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert post_check_res['status'] == SUCCESS


