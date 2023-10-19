'''operation_test.py

Any tests that do not belong to a model CRUD endpoint or an Assignment endpoint are left here

Each tests also have a reset_db fixture function. Clears the database after every test.

Certain test may require us to redo requests to setup the appropriate circumstance to test, we
do not re-assert their values as we assume they are correct based on previous.

Testing should always validate 2 things:
 - Validated the response status correctness
 - Validate the data correctness
'''

from unit.conftest import client, SUCCESS, ERROR
from unit import wrappers

def test_root():
    ''' Test root endpoint '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"connection": True}