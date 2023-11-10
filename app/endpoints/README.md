# Endpoints (5)

Endpoints are the trigger point in FastAPI that users interact to access the functions.
Each set of cruds are to have their own endpoint file as best practice.
Significant grouping of endpoint accessible functions should also be grouped together where possible.

## Expectation
- Determines the format of the body and/or url that is used
- Does preliminary data validation prior to running crud, will raise an exception when needed
- Determines the endpoint method to be used (GET, POST, PATCH, DELETE)