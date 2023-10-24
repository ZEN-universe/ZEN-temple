## ZEN Suite

Run with: `uvicorn src.main:app`
Develop with: `uvicorn src.main:app --reload --host 0.0.0.0`

If chnages to the models are made, alembic is responsible for the migrations. Use the following steps:

Create change-scripts: `alembic revision --autogenerate -m "<message>"`
Commit changes: `alembic upgrade head`

Build Docker-Container with `sudo docker build --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)" .`