## ZEN Suite

Run with: `uvicorn src.main:app`
Develop with: `uvicorn src.main:app --reload --host 0.0.0.0`

If chnages to the models are made, alembic is responsible for the migrations. Use the following steps:

Create change-scripts: `alembic revision --autogenerate -m "<message>"`
Commit changes: `alembic upgrade head`

Build Docker-Container with `docker build -t example --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" .`

Watch out, this copies your private ssh-key to the container because the required repository (ZEN garden) is private and therefore you need git-authentification.
