from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_create_trainer(reset_db, trainers_data):
    assert wrappers.create_trainer(trainers_data[0])['status'] == SUCCESS

def test_get_all_trainer(reset_db, trainers_data):
    trainers = [wrappers.create_trainer(trainers_data[i])
                for i in range(0, len(trainers_data))]

    for trainer in trainers:
        assert trainer["status"] == SUCCESS

    all_trainers = wrappers.get_all_trainers()['data']
    assert len(trainers) == len(all_trainers)

def test_get_trainer_by_trainer_id(reset_db, trainers_data):
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    ret_trainer = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])['data']
    assert trainer["name"] == ret_trainer["name"]

def test_invalid_get_trainer_by_trainer_id(reset_db, trainers_data):
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    ret_trainer = wrappers.get_trainer_by_trainer_id("TR-000")
    assert ret_trainer['status'] == ERROR

def test_delete_trainer_by_trainer_id(reset_db, trainers_data):
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    
    # Check pre-delete statue
    pre_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_trainer_by_trainer_id(trainer['trainer_id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_trainer_by_trainer_id(reset_db, trainers_data):
    trainer = wrappers.create_trainer(trainers_data[0])['data']

    # Check pre-delete statue
    pre_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_trainer_by_trainer_id("TR-000")
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert post_check_res['status'] == SUCCESS

def test_update_trainer_by_trainer_id(reset_db, trainers_data):

    # Checks that both trainers data are identical
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    new_trainer = trainers_data[1]
    assert trainer['name'] != new_trainer['name']

    new_trainer = trainers_data[1]
    update_trainer = wrappers.update_trainer_by_trainer_id(trainer['trainer_id'], new_trainer)
    assert update_trainer['status'] == SUCCESS

    assert update_trainer['data']['name'] == new_trainer['name']

def test_invalid_update_trainer_by_trainer_id(reset_db, trainers_data):
    trainer = wrappers.create_trainer(trainers_data[0])['data']
    new_trainer = trainers_data[1]
    update_trainer = wrappers.update_trainer_by_trainer_id("TR-000", new_trainer)

    assert update_trainer['status'] == ERROR

    post_check_res = wrappers.get_trainer_by_trainer_id(trainer['trainer_id'])
    assert post_check_res['status'] == SUCCESS