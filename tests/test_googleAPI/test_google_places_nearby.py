from fastapi.testclient import TestClient
from tests.test_functions.test_utils import is_non_empty_string, is_valid_coordinates

from src.app import app


client = TestClient(app)

#returns 200 status code when location and radius are valid and checks to make sure object keys are in the correct format
def test_places_nearby_200_with_default_type():
    location = "-33.8670522, 151.1957362"
    radius = 1000
    response = client.post(f"/api/places/nearby?location={location}&radius={radius}")
    assert response.status_code == 200

    nearby_places = response.json().get("locations", [])

    for place in nearby_places:
        assert isinstance(place["rating"], float | int | None)
        assert isinstance(place["user_ratings_total"], float | int | None)
        assert "tourist_attraction" in place["types"]
        assert is_non_empty_string(place["name"])
        assert is_non_empty_string(place["place_id"])
        assert is_valid_coordinates(place["geometry"]["location"])



def test_places_nearby_200_with_specified_type():
    location = "-33.8670522, 151.1957362"
    radius = 1000
    type = "hospital"
    response = client.post(f"/api/places/nearby?location={location}&radius={radius}&type={type}")
    assert response.status_code == 200

    nearby_places = response.json().get("locations", [])

    for place in nearby_places:
        assert isinstance(place["rating"], float | int | None)
        assert isinstance(place["user_ratings_total"], float | int | None)
        assert "hospital" in place["types"]
        assert is_non_empty_string(place["name"])
        assert is_non_empty_string(place["place_id"])
        assert is_valid_coordinates(place["geometry"]["location"])



def test_places_nearby_404():
    location = "33.8670522, 151.1957362"
    radius = 1000
    response = client.post(f"/api/places/nearby?location={location}&radius={radius}")
    assert response.status_code == 404
    assert response.json()["detail"] == "No results found"