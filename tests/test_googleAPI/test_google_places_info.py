from fastapi.testclient import TestClient
from tests.test_functions.test_utils import is_non_empty_string, is_valid_coordinates

from src.app import app


client = TestClient(app)

#returns status 200 and checks to make sure the output type is in the correct format
def test_places_info_200():
    address = "LS29 8EL"
    response = client.post(f"/api/places/info?address={address}")  # json= ensures the body is JSON
    assert response.status_code == 200

    place_info = response.json().get("placeInfo", [])

    for place in place_info:
        assert is_non_empty_string(place["formatted_address"])
        assert is_non_empty_string(place["name"])
        assert is_non_empty_string(place["place_id"])
        assert is_valid_coordinates(place["geometry"]["location"])


#returns status 404 when the address type is valid but doesn't exist
def test_places_info_404():
    address = "JNJBAJKBXKAJCBAKCDBOINQNCJWNANSXKJQKJ"
    response = client.post(f"/api/places/info?address={address}") # json= ensures the body is JSON
    assert response.status_code == 404
    assert response.json()["detail"] == "No results found"




#returns status 422 when address string is empty, in other words when the address field is empty.
def test_places_info_422():
    address = ""
    response = client.post(f"/api/places/info?address={address}")  # json= ensures the body is JSON
    assert response.status_code == 422
    assert response.json()["detail"] == "Address field is required"
