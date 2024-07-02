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
# fast api server should be running correctly:
# http://localhost:8000/docs
# http://localhost:8000/redoc
```

## Next Steps

### Features and Dev Experience
* add query params to search by fields
* add query params to search by complex field search (greater, less than, in, like, etc...)


### Production
Use the `Dockerfile` file to create the docker image, use as is.
```
docker build -t task_management .
```

When using the image, this are the current environmental variables available:
```
DATABASE_URL=postgresql+psycopg://<user>:<password>@<host>/<db>
```

Run migrations by executing the following command inside the container:
```python
python -m core.db
```

#### Improvements
* Use a better migration system, `alembic` seems to be the best choice.