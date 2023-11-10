'''trainer_test.py

Unit tests for each Trainer Crud Endpoint

Each tests also have a reset_db fixture function. Clears the database after every test.

Certain test may require us to redo requests to setup the appropriate circumstance to test, we
do not re-assert their values as we assume they are correct based on previous.

Testing should always validate 2 things:
 - Validated the response status correctness
 - Validate the data correctness
'''

from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_create_trainer(reset_db, trainers_data):
    ''' Testing the success case of creating an trainer '''
    assert wrappers.create_trainer(trainers_data[0])['status'] == SUCCESS

def test_get_all_trainer(reset_db, trainers_data):
    ''' Testing the success case of getting all trainers '''
    trainers = [wrappers.create_trainer(trainers_data[i])
                for i in range(0, len(trainers_data))]

    for trainer in trainers:
        assert trainer["status"] == SUCCESS

    all_trainers = wrappers.get_all_trainers()['data']
    assert len(trainers) == len(all_trainers)

def test_get_trainer_by_trainer_id(reset_db, trainers_data):
    ''' Testing the success case of getting specified trainer '''
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    ret_trainer = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer["name"] == ret_trainer["name"]

def test_invalid_get_trainer_by_trainer_id(reset_db, trainers_data):
    ''' Testing the failing case of getting specified trainer '''
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    ret_trainer = wrappers.get_trainer_by_trainer_id("TR-000")
    assert ret_trainer['status'] == ERROR

def test_delete_trainer_by_trainer_id(reset_db, trainers_data):
    ''' Testing the success case of deleting trainer '''
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    
    # Check pre-delete statue
    pre_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_trainer_by_trainer_id(trainer['trainer_id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_trainer_by_trainer_id(reset_db, trainers_data):
    ''' Testing the fail case of deleting trainer '''

    trainer = wrappers.create_trainer(trainers_data[0])['data']

    # Check pre-delete statue
    pre_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_trainer_by_trainer_id("TR-000")
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert post_check_res['status'] == SUCCESS

def test_update_trainer_by_trainer_id(reset_db, trainers_data):
    ''' Testing the success case of updating trainer '''

    # Checks that both trainers data are identical
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    new_trainer = trainers_data[1]
    assert trainer['name'] != new_trainer['name']

    # Checks update response status is correct
    new_trainer = trainers_data[1]
    update_trainer = wrappers.update_trainer_by_trainer_id(trainer['trainer_id'], new_trainer)
    assert update_trainer['status'] == SUCCESS

    # Check the update values are correct
    assert update_trainer['data']['name'] == new_trainer['name']

def test_invalid_update_trainer_by_trainer_id(reset_db, trainers_data):
    ''' Testing the fail case of updating trainer '''

    # Checks update response status is invalid, from invalid ID provided
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    new_trainer = trainers_data[1]
    update_trainer = wrappers.update_trainer_by_trainer_id("TR-000", new_trainer)
    assert update_trainer['status'] == ERROR

    # Checks that the current trainer is untouched
    curr_trainer = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert curr_trainer['data']['name'] == trainer['name']