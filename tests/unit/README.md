# Unit Tests

Unit test consist of small atomic test that tackles very specific aspects.
We are usings FastAPI TestClient which emulates the application during testing for usage.

## Expectations
- Good coverage: Ensure that the test you write comes to contact with as many lines of code.
- Validation checks: Falls under coverage, test that checks if the code succeeds as expected
- Invalidation checks: Falls under coverage, test that checks if the code fails as expected

## Notable Files
- conftest.py: Contains prelimnary configurations as well as setting up pytest fixtures to be used in the test
- wrappers.py: Contains functions that unpack and unwrap function to simplify interfacing with the apis.
- *_tests.py: Consist of the actual logic for the tests