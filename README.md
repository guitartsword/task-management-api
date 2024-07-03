# Task Management API

## Requirements
* Python (preferably >= 3.12)
* Poetry (preferably >= 1.8.3)
* Docker (preferably >= 25.0.2)


## Quick Start
```sh
docker compose up
# in another terminal
make migrate

# in case you want some data you can use
make seed_db
# fast api server should be running correctly for the developer:
# http://localhost:8000/docs
# http://localhost:8000/redoc
```

If you ran `make seed_db`, these are the user credentials to test data:
```sh
# User 1
email=user1@test.com
password=test1234
# User 2
email=user2@test.com
password=test1234
```

## Next Steps

### Dev Experience (DX)
* Configure pre-commit with black, isort, and other linting tools
* Configure mypy
* Configure pytest to add unit tests
* Configure github actions to run pre-commit and pytest
* Configure coverage for unit tests


### Features
* Add query params to search by fields (status, due_date, title, description)
* Add query params to perform complex field search (greater/less than, in, like, etc...)
* Use a better migration system, `alembic` seems to be the best choice.
* Implement full-text search for a combination of the title and description columns
  * If using `alembic`, in a migration create a trigger to update the the full-text search vector after each insert/update
  * If updating the full-text search index becomes a performance issue, consider running it periodically, manually or after `N` rows written
  * If the full-text search still has performance issue, consider using migrating to something like Elastic Search


### Production
Use the `Dockerfile` file to create the docker image for production, no other changes needed.
```
docker build -t task_management_api .
```

Configure these environmental variables:
```
DATABASE_URL=postgresql+psycopg://<user>:<password>@<host>/<db>
```

Run migrations by executing the following command inside the container:
```python
python migrate.py
```
