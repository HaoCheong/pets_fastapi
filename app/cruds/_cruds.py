"""cruds.py (4)

All the functions which directly manipulate the database. Access via main.py

- All data passed here should be valid data (Validation is done in main)
- Follows the standard: Create, Read, Update, Delete, (Assignment optional)

- db.add(): Adds to local database
- db.commit(): Commit changes in local database to actual database
- db.refresh(): Refresh local instances of object

- create_###: Create an instance of the object and add to DB
- get_all_###: Get all instance of object from table in DB
- get_###_by_id: Get specific instance of object from table in DB (via given ID)
- update_###_by_id: Update specific instance of object from table in DB (via given ID)
- delete_###_by_id: Delete specific instance of object from table in DB (via given ID)

- EXTRA: jsonable_encoder converts model.object into actual dictionary (allow for direct manipulation)
"""