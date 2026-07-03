import requests
import config
import allure
import pytest

class TestCreateOrder:
    
    @pytest.mark.parametrize("color",[
        (["BLACK"]),
        (["GREY"]),
        (["BLACK","GREY"]),
        ([])
    ])
    @allure.title('Проверка создания заказа с самокатами разных цветов')
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2029-06-06",
            "comment": "tututu",
            "color": color
        }

        response = requests.post(f'{config.BASE_URL}{config.ORDER_CREATE}',json=payload)
        assert response.status_code == 201
        assert "track" in response.json()
        