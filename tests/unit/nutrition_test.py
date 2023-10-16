from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_create_nutrition_plan(reset_db, nutrition_plans_data):
    assert wrappers.create_nutrition_plan(nutrition_plans_data[0])['status'] == SUCCESS

def test_get_all_nutrition_plan(reset_db, nutrition_plans_data):
    nutrition_plans = [wrappers.create_nutrition_plan(nutrition_plans_data[i])
                for i in range(0, len(nutrition_plans_data))]

    for nutrition_plan in nutrition_plans:
        assert nutrition_plan["status"] == SUCCESS

    all_nutrition_plans = wrappers.get_all_nutrition_plans()['data']
    assert len(nutrition_plans) == len(all_nutrition_plans)

def test_get_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']
    ret_nutrition_plan = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])['data']
    assert nutrition_plan["name"] == ret_nutrition_plan["name"]

def test_invalid_get_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']
    ret_nutrition_plan = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'] + 200)
    assert ret_nutrition_plan['status'] == ERROR

def test_delete_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']
    
    # Check pre-delete statue
    pre_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']

    # Check pre-delete statue
    pre_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])
    assert post_check_res['status'] == SUCCESS

def test_update_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):

    # Checks that both nutrition_plans data are identical
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']
    new_nutrition_plan = nutrition_plans_data[1]
    assert nutrition_plan['name'] != new_nutrition_plan['name']

    new_nutrition_plan = nutrition_plans_data[1]
    update_nutrition_plan = wrappers.update_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'], new_nutrition_plan)
    assert update_nutrition_plan['status'] == SUCCESS

    assert update_nutrition_plan['data']['name'] == new_nutrition_plan['name']

def test_invalid_update_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    nutrition_plan = wrappers.create_nutrition_plan(nutrition_plans_data[0])['data']
    new_nutrition_plan = nutrition_plans_data[1]
    update_nutrition_plan = wrappers.update_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'] + 200, new_nutrition_plan)

    assert update_nutrition_plan['status'] == ERROR

    post_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(nutrition_plan['id'])
    assert post_check_res['status'] == SUCCESS