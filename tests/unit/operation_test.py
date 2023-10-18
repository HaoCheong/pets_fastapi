'''operation_test.py

Any tests that do not belong to a model CRUD endpoint or an Assignment endpoint are left here

'''

from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_root():
    ''' Test root endpoint '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"connection": True}