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

# ========= ASSIGNING TESTS =========

# ===== PET TO OWNER =====
def test_valid_owner_assign(reset_db, pets_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    
    # Check if assignment worked
    res = wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'])
    assert res['status'] == SUCCESS

    # Check if assignment is processed on pet side
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner']['name'] == owner_full['name']

    # Check if assignment is processed on owner side
    assert pet in owner_full['pets']

def test_invalid_owner_assign(reset_db, pets_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    
    res = wrappers.assign_pet_to_owner(pet_full['id'] + 200, owner_full['id'])
    assert res['status'] == ERROR

    res = wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'] + 200)
    assert res['status'] == ERROR

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    assert pet not in owner_full['pets']

def test_valid_owner_unassign(reset_db, pets_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    
    # Assigning pets to owner
    wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner']['name'] == owner_full['name']
    assert pet in owner_full['pets']

    # Check if unassignment execution is successful
    res = wrappers.unassign_pet_from_owner(pet_full['id'], owner_full['id'])
    assert res['status'] == 200

    # Check if unassignment is successful on the data side
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    assert pet not in owner_full['pets']

def test_invalid_owner_unassign(reset_db, pets_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    
    res = wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner']['name'] == owner_full['name']
    assert pet in owner_full['pets']

    res = wrappers.unassign_pet_from_owner(pet_full['id'], owner_full['id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    assert pet not in owner_full['pets']
    

# ===== PET TO TRAINER =====

def test_valid_trainer_assign(reset_db, pets_data, trainers_data):
    pass

def test_invalid_trainer_assign(reset_db, pets_data, trainers_data):
    pass

def test_valid_trainer_unassign(reset_db, pets_data, trainers_data):
    pass

def test_invalid_trainer_unassign(reset_db, pets_data, trainers_data):
    pass

# ===== PET TO NUTRITION =====

def test_valid_nutrition_assign(reset_db, pets_data, nutrition_plans_data):
    pass

def test_valid_full_assign(reset_db, pets_data, owners_data, trainers_data, nutrition_plans_data):
    pass

