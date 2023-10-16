from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"connection": True}

def test_create_owner(reset_db, owners_data):
    assert wrappers.create_owner(owners_data[0])['status'] == SUCCESS

def test_get_all_owner(reset_db, owners_data):
    owners = [wrappers.create_owner(owners_data[i])
                for i in range(0, len(owners_data))]

    for owner in owners:
        assert owner["status"] == SUCCESS

    all_owners = wrappers.get_all_owners()
    assert len(owners) == len(all_owners)

def test_get_owner_by_owner_id(reset_db, owners_data):
    owner = wrappers.create_owner(owners_data[0])['data']
    ret_owner = wrappers.get_owner_by_owner_id(owner['id'])['data']
    assert owner["email"] == ret_owner["email"]

def test_invalid_get_owner_by_owner_id(reset_db, owners_data):
    owner = wrappers.create_owner(owners_data[0])['data']
    ret_owner = wrappers.get_owner_by_owner_id(owner['id'] + 200)
    assert ret_owner['status'] == ERROR

def test_delete_owner_by_owner_id(reset_db, owners_data):
    owner = wrappers.create_owner(owners_data[0])['data']
    
    # Check pre-delete statue
    pre_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_owner_by_owner_id(owner['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_owner_by_owner_id(reset_db, owners_data):
    owner = wrappers.create_owner(owners_data[0])['data']

    # Check pre-delete statue
    pre_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion event
    delete_res = wrappers.delete_owner_by_owner_id(owner['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert post_check_res['status'] == SUCCESS

def test_update_owner_by_owner_id(reset_db, owners_data):

    # Checks that both owners data are identical
    owner = wrappers.create_owner(owners_data[0])['data']
    new_owner = owners_data[1]
    assert owner['email'] != new_owner['email']

    new_owner = owners_data[1]
    update_owner = wrappers.update_owner_by_owner_id(owner['id'], new_owner)
    assert update_owner['status'] == SUCCESS

    assert update_owner['data']['email'] == new_owner['email']

def test_invalid_update_owner_by_owner_id(reset_db, owners_data):
    owner = wrappers.create_owner(owners_data[0])['data']
    new_owner = owners_data[1]
    update_owner = wrappers.update_owner_by_owner_id(owner['id'] + 200, new_owner)

    assert update_owner['status'] == ERROR

    post_check_res = wrappers.get_owner_by_owner_id(owner['id'])
    assert post_check_res['status'] == SUCCESS