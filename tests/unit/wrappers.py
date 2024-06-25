'''wrappers.py

Contains functions that emulate a request to the client without actually needed create a request.

'''

from tests.client_fixture import client, SUCCESS
import json


def unpack(function):
    ''' Wrapper to unpack the json values into parsable dictionary. Easier for testing '''
    def get_data(*args):
        resp = function(*args)
        if resp.status_code != SUCCESS:
            data = json.loads(resp.text)
            return {'status': resp.status_code,
                    'detail': data['detail']
                    }
        else:
            return {'status': resp.status_code,
                    'data': json.loads(resp.text)
                    }
    return get_data


''' ========== OWNER WRAPPERS ========== '''


@unpack
def create_owner(owner_data):
    ''' Wrapper to emulate creating an owner '''
    return client.post('/owner', json=owner_data)


@unpack
def get_all_owners():
    ''' Wrapper to emulate getting all owners '''
    return client.get('/owners')


@unpack
def get_owner_by_owner_id(owner_id):
    ''' Wrapper to emulate getting specified owner '''
    return client.get(f'/owner/{owner_id}')


@unpack
def delete_owner_by_owner_id(owner_id):
    ''' Wrapper to emulate deleting specified owner '''
    return client.delete(f'/owner/{owner_id}')


@unpack
def update_owner_by_owner_id(owner_id, owner_dict):
    ''' Wrapper to emulate updating specified owner '''
    return client.patch(f'/owner/{owner_id}', json=owner_dict)


''' ========== PET WRAPPERS ========== '''


@unpack
def create_pet(pets_data):
    ''' Wrapper to emulate creating a pet '''
    return client.post('/pet', json=pets_data)


@unpack
def get_all_pets():
    ''' Wrapper to emulate getting all pets '''
    return client.get('/pets')


@unpack
def get_pet_by_pet_id(pet_id):
    ''' Wrapper to emulate getting specified pet '''
    return client.get(f'/pet/{str(pet_id)}')


@unpack
def delete_pet_by_pet_id(pet_id):
    ''' Wrapper to emulate deleting specified pet '''
    return client.delete(f'/pet/{pet_id}')


@unpack
def update_pet_by_pet_id(pet_id, pet_dict):
    ''' Wrapper to emulate updating specified pet '''
    return client.patch(f'/pet/{pet_id}', json=pet_dict)


''' ========== TRAINERS WRAPPERS ========== '''


@unpack
def create_trainer(trainer_data):
    ''' Wrapper to emulate creating a trainer '''
    return client.post('/trainer', json=trainer_data)


@unpack
def get_all_trainers():
    ''' Wrapper to emulate getting all trainers '''
    return client.get('/trainers')


@unpack
def get_trainer_by_trainer_id(trainer_id):
    ''' Wrapper to emulate getting specified trainer '''
    return client.get(f'/trainer/{str(trainer_id)}')


@unpack
def delete_trainer_by_trainer_id(trainer_id):
    ''' Wrapper to emulate deleting specified trainer '''
    return client.delete(f'/trainer/{trainer_id}')


@unpack
def update_trainer_by_trainer_id(trainer_id, trainer_dict):
    ''' Wrapper to emulate updating specified trainer '''
    return client.patch(f'/trainer/{trainer_id}', json=trainer_dict)


''' ============ NUTRITION PLAN WRAPPERS ============ '''


@unpack
def create_nutrition_plan(nutrition_plan_data):
    ''' Wrapper to emulate creating a trainer '''
    return client.post('/nutrition_plan', json=nutrition_plan_data)


@unpack
def get_all_nutrition_plans():
    ''' Wrapper to emulate getting all trainers '''
    return client.get('/nutrition_plans')


@unpack
def get_nutrition_plan_by_nutrition_plan_id(nutrition_plan_id):
    ''' Wrapper to emulate getting specified trainer '''
    return client.get(f'/nutrition_plan/{str(nutrition_plan_id)}')


@unpack
def delete_nutrition_plan_by_nutrition_plan_id(nutrition_plan_id):
    ''' Wrapper to emulate deleting specified trainer '''
    return client.delete(f'/nutrition_plan/{nutrition_plan_id}')


@unpack
def update_nutrition_plan_by_nutrition_plan_id(nutrition_plan_id, nutrition_plan_dict):
    ''' Wrapper to emulate updating specified trainer '''
    return client.patch(f'/nutrition_plan/{nutrition_plan_id}', json=nutrition_plan_dict)


''' ============ ASSIGNMENT WRAPPERS ============ '''


@unpack
def assign_pet_to_owner(pet_id, owner_id):
    ''' Wrapper to emulate assigning pet to owner '''
    return client.post(f'/assignToOwner/{pet_id}/{owner_id}')


@unpack
def unassign_pet_from_owner(pet_id, owner_id):
    ''' Wrapper to emulate unassigning pet from owner '''
    return client.post(f'/unassignFromOwner/{pet_id}/{owner_id}')


@unpack
def assign_pet_to_trainer(pet_id, trainer_id):
    ''' Wrapper to emulate assigning pet to trainer '''
    return client.post(f'/assignToTrainer/{pet_id}/{trainer_id}')


@unpack
def unassign_pet_from_trainer(pet_id, trainer_id):
    ''' Wrapper to emulate unassigning pet to trainer '''
    return client.post(f'/unassignFromTrainer/{pet_id}/{trainer_id}')


@unpack
def assign_pet_to_nutrition_plan(pet_id, nutrition_plan_id):
    ''' Wrapper to emulate assigning pet to nutritional plan '''
    return client.post(f'/assignToNutritionPlan/{pet_id}/{nutrition_plan_id}')


@unpack
def unassign_pet_from_nutrition_plan(pet_id):
    ''' Wrapper to emulate unassigning pet to nutritional plan '''
    return client.post(f'/unassignFromNutritionPlan/{pet_id}')
