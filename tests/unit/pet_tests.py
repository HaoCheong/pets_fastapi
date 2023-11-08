'''pet_test.py

Unit tests for each Pet Crud Endpoint

Each tests also have a reset_db fixture function. Clears the database after every test.

Certain test may require us to redo requests to setup the appropriate circumstance to test, we
do not re-assert their values as we assume they are correct based on previous.

Testing should always validate 2 things:
 - Validated the response status correctness
 - Validate the data correctness
'''

from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_create_pet(reset_db, pets_data):
    ''' Testing the success case of creating a pet '''
    assert wrappers.create_pet(pets_data[0])['status'] == SUCCESS

def test_get_all_pet(reset_db, pets_data):
    ''' Testing the success case of getting all pets '''

    # Passes all pet test data into database
    pets = [wrappers.create_pet(pets_data[i])
                for i in range(0, len(pets_data))]

    # Checks all responses succeeds
    for pet in pets:
        assert pet["status"] == SUCCESS

    # Compare return list with input list
    all_pets = wrappers.get_all_pets()['data']
    assert len(pets) == len(all_pets)

def test_get_pet_by_pet_id(reset_db, pets_data):
    ''' Testing the success case of getting specified pet '''
    pet = wrappers.create_pet(pets_data[0])['data']
    ret_pet = wrappers.get_pet_by_pet_id(pet['id'])['data']
    assert pet["name"] == ret_pet["name"]

def test_invalid_get_pet_by_pet_id(reset_db, pets_data):
    ''' Testing the failing case of getting specified pet '''
    pet = wrappers.create_pet(pets_data[0])['data']
    ret_pet = wrappers.get_pet_by_pet_id(pet['id'] + 200)
    assert ret_pet['status'] == ERROR

def test_delete_pet_by_pet_id(reset_db, pets_data):
    ''' Testing the success case of deleting pet '''

    pet = wrappers.create_pet(pets_data[0])['data']
    
    # Check pre-delete status
    pre_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_pet_by_pet_id(pet['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_pet_by_pet_id(reset_db, pets_data):
    ''' Testing the fail case of deleting pet '''
    pet = wrappers.create_pet(pets_data[0])['data']

    # Check pre-delete statue
    pre_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_pet_by_pet_id(pet['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_pet_by_pet_id(pet['id'])
    assert post_check_res['status'] == SUCCESS

def test_update_pet_by_pet_id(reset_db, pets_data):
    ''' Testing the success case of updating pet '''

    # Checks that both pets data are identical
    pet = wrappers.create_pet(pets_data[0])['data']
    new_pet = pets_data[1]
    assert pet['name'] != new_pet['name']

    # Checks update response status is correct
    new_pet = pets_data[1]
    update_pet = wrappers.update_pet_by_pet_id(pet['id'], new_pet)
    assert update_pet['status'] == SUCCESS

    # Check the update values are correct
    assert update_pet['data']['name'] == new_pet['name']

def test_invalid_update_pet_by_pet_id(reset_db, pets_data):
    ''' Testing the fail case of updating pet '''

    # Checks update response status is invalid, from invalid ID provided
    pet = wrappers.create_pet(pets_data[0])['data']
    new_pet = pets_data[1]
    update_pet = wrappers.update_pet_by_pet_id(pet['id'] + 200, new_pet)
    assert update_pet['status'] == ERROR

    # Checks that the current pet is untouched
    curr_pet = wrappers.get_pet_by_pet_id(pet['id'])
    assert curr_pet['data']['name'] == pet['name']


