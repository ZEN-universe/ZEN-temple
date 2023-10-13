from fastapi.testclient import TestClient
from src.main import app

base = "dataset"


def create_dataset():
    pass


def test_dataset_list():
    client = TestClient(app)

    response = client.get(f"{base}/list")

    assert response.status_code == 200
