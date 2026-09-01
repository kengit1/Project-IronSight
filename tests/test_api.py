"""
Basic smoke tests for the Gym Equipment API.
Run with: pytest
"""

import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Backend Server is running!"}


def test_list_equipment():
    response = client.get("/equipment")
    assert response.status_code == 200
    body = response.json()
    assert body["count"] == 13
    assert "Lat Pull Down" in body["equipment"]


def test_get_equipment_by_name_case_insensitive():
    response = client.get("/equipment/lat pull down")
    assert response.status_code == 200
    assert response.json()["equipment"] == "Lat Pull Down"


def test_get_equipment_unknown_name_falls_back():
    response = client.get("/equipment/not-a-real-machine")
    assert response.status_code == 200
    assert response.json()["primary_muscle"] == "Unknown"


def test_predict_with_fake_image():
    # A tiny 1x1 PNG so we don't need a real image file for the test.
    fake_png = (
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
        b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xcf\xc0"
        b"\x00\x00\x03\x01\x01\x00\x18\xdd\x8d\xb0\x00\x00\x00\x00IEND\xaeB`\x82"
    )
    response = client.post(
        "/predict",
        files={"file": ("test.png", io.BytesIO(fake_png), "image/png")},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "success"
    assert body["data"]["equipment"] == "Lat Pull Down"


def test_predict_rejects_non_image_file():
    response = client.post(
        "/predict",
        files={"file": ("test.txt", io.BytesIO(b"not an image"), "text/plain")},
    )
    assert response.status_code == 400


def test_predict_rejects_empty_file():
    response = client.post(
        "/predict",
        files={"file": ("empty.png", io.BytesIO(b""), "image/png")},
    )
    assert response.status_code == 400