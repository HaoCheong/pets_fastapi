'''owner_test.py

Unit tests for each Owner Crud Endpoint

'''

from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_create_owner(reset_db, owners_data):
    ''' Testing the success case of creating an owner '''
    assert wrappers.create_owner(owners_data[0])['status'] == SUCCESS

def test_get_all_owner(reset_db, owners_data):
    ''' Testing the success case of getting all owners '''
    
    # Passes all owner test data into database
    owners = [wrappers.create_owner(owners_data[i])
                for i in range(0, len(owners_data))]

    # Checks all responses succeeds
    for owner in owners:
        assert owner["status"] == SUCCESS

    # Compare return list with input list
    all_owners = wrappers.get_all_owners()
    assert len(owners) == len(all_owners)

def test_get_owner_by_owner_id(reset_db, owners_data):
    ''' Testing the success case of getting specified owner '''
    owner = wrappers.create_owner(owners_data[0])['data']
    ret_owner = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert owner["email"] == ret_owner["email"]

def test_invalid_get_owner_by_owner_id(reset_db, owners_data):
    ''' Testing the failing case of getting specified owner '''
    owner = wrappers.create_owner(owners_data[0])['data']
    ret_owner = wrappers.get_owner_by_owner_id(owner['id'] + 200)
    assert ret_owner['status'] == ERROR

def test_delete_owner_by_owner_id(reset_db, owners_data):
    ''' Testing the success case of deleting owner '''
    owner = wrappers.create_owner(owners_data[0])['data']
    
    # Check pre-delete status
    pre_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_owner_by_owner_id(owner['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_owner_by_owner_id(reset_db, owners_data):
    ''' Testing the fail case of deleting owner '''

    owner = wrappers.create_owner(owners_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_owner_by_owner_id(owner['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert post_check_res['status'] == SUCCESS

def test_update_owner_by_owner_id(reset_db, owners_data):
    ''' Testing the success case of updating owner '''

    # Checks that created owner and new owner are different
    owner = wrappers.create_owner(owners_data[0])['data']
    new_owner = owners_data[1]
    assert owner['email'] != new_owner['email']

    # Checks update response status is correct
    new_owner = owners_data[1]
    update_owner = wrappers.update_owner_by_owner_id(owner['id'], new_owner)
    assert update_owner['status'] == SUCCESS

    # Check the update values are correct
    assert update_owner['data']['email'] == new_owner['email']

def test_invalid_update_owner_by_owner_id(reset_db, owners_data):
    ''' Testing the fail case of updating owner '''

    # Checks update response status is invalid, from invalid ID provided
    owner = wrappers.create_owner(owners_data[0])['data']
    new_owner = owners_data[1]
    update_owner = wrappers.update_owner_by_owner_id(owner['id'] + 200, new_owner)
    assert update_owner['status'] == ERROR

    # Checks that the current owner is untouched
    curr_owner = wrappers.get_owner_by_owner_id(owner['id'])
    assert curr_owner['data']['name'] == owner['name']