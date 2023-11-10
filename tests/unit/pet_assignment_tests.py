'''pet_assignment_test.py

Test the assignment of pets to various other models. Cover testing for all relationships

Pets Assignments also have dependencies in what order assignments are made 
1. Pets -> Owner
2. Pets -> Trainer (Trainer requires a pet that has an owner)
3. Pets -> Nutrition Plan (Nutrition Plan requires a pet that has an trainer)

Most endpoints consists of two tests:
 - Valid Test: Test case of success scenarios
 - Invalid test: Test cases of failing scenarios. Catches every expected error.
'''

from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers


''' ========== PETS TO OWNER TESTS ========== '''

def test_valid_owner_assign(reset_db, pets_data, owners_data):
    ''' Test successful assigning pet to owner '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']

    # Getting the expanded version of the pet and owner
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']

    # Check pet start with null owner
    print("AHH",owner_full)
    assert len(owner_full['pets']) == 0
    assert pet_full['owner'] == None
    
    # Check if assignment request response succeeded
    res = wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'])
    assert res['status'] == SUCCESS

    # Check owner assignment is reflected in the pet's return value
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    assert pet_full['owner']['name'] == owner_full['name']

    # Check owner assignment is reflected in the owner's return value
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet in owner_full['pets']

def test_invalid_owner_assign(reset_db, pets_data, owners_data):
    ''' Test failing assigning pet to owner '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']

    # Getting the expanded version of the pet and owner
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']

    # Check pet start with null owner
    assert pet_full['owner'] == None
    
    # Check if response fails, provided invalid pet ID
    res = wrappers.assign_pet_to_owner(pet_full['id'] + 200, owner_full['id'])
    assert res['status'] == ERROR

    # Check if response fails, provided invalid owner ID
    res = wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'] + 200)
    assert res['status'] == ERROR

    # Check if pets and owner are left unaffected
    curr_pet = wrappers.get_pet_by_pet_id(pet['id'])['data']
    curr_owner = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert curr_pet['owner'] == None
    assert pet not in curr_owner['pets']

def test_valid_owner_unassign(reset_db, pets_data, owners_data):
    ''' Test successful unassigning pet to owner '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']

    # Getting the expanded version of the pet and owner
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']

    # Assigning pets to owner 
    wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'])
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']

    # Check if unassignment execution is successful
    res = wrappers.unassign_pet_from_owner(pet_full['id'], owner_full['id'])
    assert res['status'] == SUCCESS

    # Check if unassignment is successful on the data side
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner'] == None
    assert pet not in owner_full['pets']

def test_invalid_owner_unassign(reset_db, pets_data, owners_data):
    ''' Test failing unassigning pet to owner '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']

    # Getting the expanded version of the pet and owner
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']

    # Check pet start with null owner
    assert pet_full['owner'] == None
    
    # Assiging pets to owner
    wrappers.assign_pet_to_owner(pet_full['id'], owner_full['id'])

    # Check if response fails, provided invalid pet ID 
    res = wrappers.unassign_pet_from_owner(pet_full['id'] + 200, owner_full['id'])
    assert res['status'] == ERROR

    # Check if response fails, provided invalid owner ID
    res = wrappers.unassign_pet_from_owner(pet_full['id'], owner_full['id'] + 200)
    assert res['status'] == ERROR

    # Check if pets and owner are left unaffected
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    owner_full = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert pet_full['owner']['name'] == owner_full['name']
    assert pet in owner_full['pets']
    

''' ========== PET TO TRAINER TESTS ========== '''

def test_valid_trainer_assign(reset_db, pets_data, trainers_data, owners_data):
    ''' Testing successful assigning of pets to trainer '''

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
    ''' Testing failing assigning of pets to trainer '''
    
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
    ''' Testing successful unassigning of pets to trainer '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']

    # Assigning Pets to Trainer
    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer_full['trainer_id'])

    # Check if assignment request response succeeded
    res = wrappers.unassign_pet_from_trainer(pet_full['id'], trainer_full['trainer_id'])
    res['status'] == SUCCESS

    # Check trainer assignment is reflected in the pet's return value
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer not in pet_full['trainers']

    # Check trainer assignment is reflected in the trainer's return value
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    assert pet not in trainer_full['pets']

def test_invalid_trainer_unassign(reset_db, pets_data, trainers_data, owners_data):
    ''' Test failing unassigning pet to trainer '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']

    # Assiging pets to trainer
    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer_full['trainer_id'])

    # Check if response fails, provided invalid pet ID 
    res = wrappers.unassign_pet_from_trainer(pet_full['id'] + 200, trainer_full['trainer_id'])
    res['status'] == ERROR

    # Check if response fails, provided invalid trainer ID 
    res = wrappers.unassign_pet_from_trainer(pet_full['id'], "TR-000")
    res['status'] == ERROR

    # Check if pets and trainer are left unaffected
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    trainer_full = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer in pet_full['trainers']
    assert pet in trainer_full['pets']


''' ========== PET TO NUTRITION PLAN TESTS ========== '''

def test_valid_nutrition_assign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    ''' Test successful assigning pet to nutrition plan '''
    
    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    # Getting the expanded version of the pet and nutrition plan
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']

    # Check pet and nutrition start with null   
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

    # Check if assignment request response succeeded
    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])
    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'])
    res['status'] == SUCCESS

    # Check nutrition plan assignment is reflected in the pet's return value
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == pet

    # Check nutrition plan assignment is reflected in the nutrition plan's return value
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    assert pet_full['nutrition_plan'] == nutrition_plan


def test_invalid_nutrition_assign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    ''' Test failing assigning pet to nutrition plan '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    # Getting the expanded version of the pet and nutrition plan
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']

    # Assign Pets to Trainer
    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])

    # Check if response fails, provided invalid pet ID
    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'] + 200, nutrition_plan_full['id'])
    res['status'] == ERROR

    # Check if response fails, provided invalid nutrition plan ID
    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'] + 200)
    res['status'] == ERROR

    # Check if pets and owner are left unaffected
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

def test_valid_nutrition_unassign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    ''' Test successful unassigning pet to nutrition plan '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    # Getting the expanded version of the pet and nutrition plan
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']

    # Assign Pet to Trainer
    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])
    res = wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'])

    # Check if unassignment execution is successful
    res = wrappers.unassign_pet_from_nutrition_plan(pet_full['id'])
    res['status'] == SUCCESS

    # Check if unassignment is successful on the data side
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == None
    assert pet_full['nutrition_plan'] == None

def test_invalid_nutrition_unassign(reset_db, pets_data, trainers_data, nutrition_plans_data, owners_data):
    ''' Test failing unassigning pet to nutrition plan '''

    # Setup
    pet = wrappers.create_pet(pets_data[0])['data']
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    owner = wrappers.create_owner(owners_data[0])['data']
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    # Getting the expanded version of the pet and owner
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']

    # Assigning Pets to Nutrition Plan
    wrappers.assign_pet_to_owner(pet_full['id'], owner['id'])
    wrappers.assign_pet_to_trainer(pet_full['id'], trainer['trainer_id'])
    wrappers.assign_pet_to_nutrition_plan(pet_full['id'], nutrition_plan_full['id'])

    # Check if response fails, provided invalid pet ID 
    res = wrappers.unassign_pet_from_nutrition_plan(pet_full['id'] + 200)
    res['status'] == ERROR

    # Check if pets and trainer are left unaffected
    pet_full = wrappers.get_pet_by_pet_id(pet['id'])['data']
    nutrition_plan_full = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan_full['pet'] == pet
    assert pet_full['nutrition_plan'] == nutrition_plan

