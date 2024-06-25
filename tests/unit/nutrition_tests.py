'''nutrition_test.py

Unit tests for each Nutrition Plan Crud Endpoint

Each tests also have a reset_db fixture function. Clears the database after every test.

Certain test may require us to redo requests to setup the appropriate circumstance to test, we
do not re-assert their values as we assume they are correct based on previous.

Testing should always validate 2 things:
 - Validated the response status correctness
 - Validate the data correctness
'''

from tests.client_fixture import client, SUCCESS, ERROR, reset_db
from tests.data_fixtures import nutrition_plans_data
from tests.unit import wrappers


def test_create_nutrition_plan(reset_db, nutrition_plans_data):
    ''' Testing the success case of creating a nutrition plan '''
    assert wrappers.create_nutrition_plan(nutrition_plans_data[0])[
        'status'] == SUCCESS


def test_get_all_nutrition_plan(reset_db, nutrition_plans_data):
    ''' Testing the success case of getting all nutrition plan '''

    # Passes all nutrition plan test data into database
    nutrition_plans = [wrappers.create_nutrition_plan(nutrition_plans_data[i])
                       for i in range(0, len(nutrition_plans_data))]

    # Checks all responses succeeds
    for nutrition_plan in nutrition_plans:
        assert nutrition_plan["status"] == SUCCESS

    # Compare return list with input list
    all_nutrition_plans = wrappers.get_all_nutrition_plans()['data']
    assert len(nutrition_plans) == len(all_nutrition_plans)


def test_get_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    ''' Testing the success case of getting specified nutrition plan '''
    nutrition_plan = wrappers.create_nutrition_plan(
        nutrition_plans_data[0])['data']
    ret_nutrition_plan = wrappers.get_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'])['data']
    assert nutrition_plan["name"] == ret_nutrition_plan["name"]


def test_invalid_get_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    ''' Testing the failing case of getting specified nutrition plan '''
    nutrition_plan = wrappers.create_nutrition_plan(
        nutrition_plans_data[0])['data']
    ret_nutrition_plan = wrappers.get_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'] + 200)
    assert ret_nutrition_plan['status'] == ERROR


def test_delete_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    ''' Testing the success case of deleting nutrition plan '''
    nutrition_plan = wrappers.create_nutrition_plan(
        nutrition_plans_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'])
    assert post_check_res['status'] == ERROR


def test_invalid_delete_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    ''' Testing the fail case of deleting nutrition plan '''

    nutrition_plan = wrappers.create_nutrition_plan(
        nutrition_plans_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'])
    assert post_check_res['status'] == SUCCESS


def test_update_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    ''' Testing the success case of updating nutrition plan '''

    # Checks that created nutrition plan and new nutrition plan are different
    nutrition_plan = wrappers.create_nutrition_plan(
        nutrition_plans_data[0])['data']
    new_nutrition_plan = nutrition_plans_data[1]
    assert nutrition_plan['name'] != new_nutrition_plan['name']

    # Checks update response status is correct
    new_nutrition_plan = nutrition_plans_data[1]
    update_nutrition_plan = wrappers.update_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'], new_nutrition_plan)
    assert update_nutrition_plan['status'] == SUCCESS

    # Check the update values are correct
    assert update_nutrition_plan['data']['name'] == new_nutrition_plan['name']


def test_invalid_update_nutrition_plan_by_nutrition_plan_id(reset_db, nutrition_plans_data):
    ''' Testing the fail case of updating nutrition plan '''

    # Checks update response status is invalid, from invalid ID provided
    nutrition_plan = wrappers.create_nutrition_plan(
        nutrition_plans_data[0])['data']
    new_nutrition_plan = nutrition_plans_data[1]
    update_nutrition_plan = wrappers.update_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'] + 200, new_nutrition_plan)
    assert update_nutrition_plan['status'] == ERROR

    # Checks that the current nutrition plan is untouched
    curr_nutrition_plan = wrappers.get_nutrition_plan_by_nutrition_plan_id(
        nutrition_plan['id'])
    assert curr_nutrition_plan['data']['name'] == nutrition_plan['name']
