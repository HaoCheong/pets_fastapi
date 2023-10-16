from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

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

def test_valid_trainer_assign(reset_db, pets_data, trainers_data, owners_data):

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer not in pet_full['trainers']
    assert pet not in trainer_full['pets']

    # Check assignment execution is successful
    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    res = wrappers.assign_pet_to_trainer(pet_full['id'], trainer_full['trainer_id'])
    assert res['status'] == SUCCESS

    # Check assignment values are correct
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer in pet_full['trainers']
    assert pet in trainer_full['pets']

def test_invalid_trainer_assign(reset_db, pets_data, trainers_data, owners_data):

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer not in pet_full['trainers']
    assert pet not in trainer_full['pets']

    # Check if assigning pet to trainer without owner has failed
    res = wrappers.assign_pet_to_trainer(pet_full['id'], trainer_full['trainer_id'])
    assert res['status'] == ERROR

    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])

    # Check if assigning invalid pet to trainer has failed
    res = wrappers.assign_pet_to_trainer(pet_full['id'] + 1, trainer_full['trainer_id'])
    assert res['status'] == ERROR

    # Check if assigning to invalid trainer has failed
    res = wrappers.assign_pet_to_trainer(pet_full['id'],"TR-000")
    assert res['status'] == ERROR

def test_valid_trainer_unassign(reset_db, pets_data, trainers_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer not in pet_full['trainers']
    assert pet not in trainer_full['pets']

    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer_full['trainer_id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer in pet_full['trainers']
    assert pet in trainer_full['pets']

    res = wrappers.unassign_pet_from_trainer(pet_full['id'], trainer_full['trainer_id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    res['status'] == SUCCESS

    assert trainer not in pet_full['trainers']
    assert pet not in trainer_full['pets']

def test_invalid_trainer_unassign(reset_db, pets_data, trainers_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer not in pet_full['trainers']
    assert pet not in trainer_full['pets']

    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer_full['trainer_id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer in pet_full['trainers']
    assert pet in trainer_full['pets']

    res = wrappers.unassign_pet_from_trainer(pet_full['id'] + 200, trainer_full['trainer_id'])
    res['status'] == ERROR

    res = wrappers.unassign_pet_from_trainer(pet_full['id'], "TR-000")
    res['status'] == ERROR

    assert trainer in pet_full['trainers']
    assert pet in trainer_full['pets']


# ===== PET TO NUTRITION =====

def test_valid_nutrition_assign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])
    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'])
    res['status'] == SUCCESS

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == pet
    assert pet_full['nutrition_plan'] == nutrition_plan


def test_invalid_nutrition_assign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])

    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'] + 200, nutrition_plan_full['id'])
    res['status'] == ERROR

    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'] + 200)
    res['status'] == ERROR

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

def test_valid_nutrition_unassign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])
    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == pet
    assert pet_full['nutrition_plan'] == nutrition_plan

    res = wrappers.unassign_pet_from_nutrition_plan(pet_full['id'])
    res['status'] == SUCCESS

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

def test_invalid_nutrition_unassign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])
    wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == pet
    assert pet_full['nutrition_plan'] == nutrition_plan

    res = wrappers.unassign_pet_from_nutrition_plan(pet_full['id'] + 200)
    res['status'] == ERROR

    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == pet
    assert pet_full['nutrition_plan'] == nutrition_plan

