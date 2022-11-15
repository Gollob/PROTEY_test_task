import requests

class TestGeoApi:

    def test_get_adrress(self, adrress, place_id):
        request_url = f"https://nominatim.openstreetmap.org/?addressdetails=1&q={adrress}&format=json&limit=1"
        response = requests.get(request_url)
        assert response.status_code == 200
        assert response.text.count(str(place_id)) == 1  #проверяем количество совпадений с place_id

    def test_get_coordinates(self, lat, lon, place_id):
        request_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        response = requests.get(request_url)
        assert response.status_code == 200
        assert response.json().get('place_id') == place_id #проверяем place_id
