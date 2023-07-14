import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from bson import ObjectId
from appgallery_spy.api import app

from unittest import mock


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def mock_review_collection():
    # Create a mock review collection
    mock_collection = mock.Mock()

    # Define the test data
    test_data = [
        {
            "_id": ObjectId("64b053a0248bd2bc00543046"),
            "username": "User 1",
            "date": datetime(2023, 7, 15, 10, 0, 0),
            "review_text": "This is review 1",
            "rating": 4,
        },
        {
            "_id": ObjectId("64b053a0248bd2bc00543047"),
            "username": "User 2",
            "date": datetime(2023, 7, 14, 9, 0, 0),
            "review_text": "This is review 2",
            "rating": 3,
        },
    ]

    # Mock the find().sort().limit() chain to return the test data
    mock_collection.find.return_value.sort.return_value.limit.return_value = test_data

    return mock_collection


def test_get_recent_reviews(test_client, mock_review_collection, monkeypatch):
    # Monkeypatch the review_collection to use the mock collection
    monkeypatch.setattr("appgallery_spy.api.get_recent_reviews", mock_review_collection)

    response = test_client.post("/reviews/recent", json={"count": 2})
    assert response.status_code == 200

    reviews = response.json()
    assert len(reviews) == 2

    assert reviews[0]["username"] == "User 1"
    assert reviews[0]["date"] == "2023-07-15T10:00:00"
    assert reviews[0]["review_text"] == "This is review 1"
    assert reviews[0]["rating"] == 4

    assert reviews[1]["username"] == "User 2"
    assert reviews[1]["date"] == "2023-07-14T09:00:00"
    assert reviews[1]["review_text"] == "This is review 2"
    assert reviews[1]["rating"] == 3
