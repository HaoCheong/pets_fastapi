from unit.conftest import client, SUCCESS
import json

# Wrapper to convert the json values into parsable dictionary
def unpack(function):
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

# ============ OWNER ============

@unpack
def create_owner(owner_data):
    return client.post('/owner', json=owner_data)


@unpack
def get_all_owners():
    return client.get('/owners')


@unpack
def get_owner_by_owner_id(owner_id):
    return client.get(f'/owner/{owner_id}')


@unpack
def delete_owner_by_owner_id(owner_id):
    return client.delete(f'/owner/{owner_id}')


@unpack
def update_owner_by_owner_id(owner_id, owner_dict):
    return client.patch(f'/owner/{owner_id}', json=owner_dict)

# ============ PETS ============

@unpack
def create_pet(pets_data):
    return client.post('/pet', json=pets_data)


@unpack
def get_all_pets():
    return client.get('/pets')


@unpack
def get_pet_by_pet_id(pet_id):
    return client.get(f'/pet/{str(pet_id)}')


@unpack
def delete_pet_by_pet_id(pet_id):
    return client.delete(f'/pet/{pet_id}')


@unpack
def update_pet_by_pet_id(pet_id, pet_dict):
    return client.patch(f'/pet/{pet_id}', json=pet_dict)

# ============ TRAINERS ============

@unpack
def create_trainer(trainer_data):
    return client.post('/trainer', json=trainer_data)


@unpack
def get_all_trainers():
    return client.get('/trainers')


@unpack
def get_trainer_by_trainer_id(trainer_id):
    return client.get(f'/trainer/{str(trainer_id)}')


@unpack
def delete_trainer_by_trainer_id(trainer_id):
    return client.delete(f'/trainer/{trainer_id}')


@unpack
def update_trainer_by_trainer_id(trainer_id, trainer_dict):
    return client.patch(f'/trainer/{trainer_id}', json=trainer_dict)

# ============ NUTRITION PLAN ============

@unpack
def create_nutrition_plan(nutrition_plan_data):
    return client.post('/nutrition_plan', json=nutrition_plan_data)


@unpack
def get_all_nutrition_plans():
    return client.get('/nutrition_plans')


@unpack
def get_nutrition_plan_by_nutrition_plan_id(nutrition_plan_id):
    return client.get(f'/nutrition_plan/{str(nutrition_plan_id)}')


@unpack
def delete_nutrition_plan_by_nutrition_plan_id(nutrition_plan_id):
    return client.delete(f'/nutrition_plan/{nutrition_plan_id}')


@unpack
def update_nutrition_plan_by_nutrition_plan_id(nutrition_plan_id, nutrition_plan_dict):
    return client.patch(f'/nutrition_plan/{nutrition_plan_id}', json=nutrition_plan_dict)

# ======== ASSIGNMENT ========

@unpack
def assign_pet_to_owner(pet_id, owner_id):
    return client.post(f'/assignToOwner/{pet_id}/{owner_id}')

@unpack
def unassign_pet_from_owner(pet_id, owner_id):
    return client.post(f'/unassignFromOwner/{pet_id}/{owner_id}')

@unpack
def assign_pet_to_trainer(pet_id, trainer_id):
    return client.post(f'/assignToTrainer/{pet_id}/{trainer_id}')

@unpack
def unassign_pet_from_trainer(pet_id, trainer_id):
    return client.post(f'/unassignFromTrainer/{pet_id}/{trainer_id}')

@unpack
def assign_pet_to_nutrition_plan(pet_id, nutrition_plan_id):
    return client.post(f'/assignToNutritionPlan/{pet_id}/{nutrition_plan_id}')

@unpack
def unassign_pet_from_nutrition_plan(pet_id):
    return client.post(f'/unassignFromNutritionPlan/{pet_id}')