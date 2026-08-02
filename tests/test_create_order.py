import requests
from urls import Urls
from data import OrderData
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
        with allure.step('Подготовка тестовых данных'):
            payload = {
                "firstName": OrderData.FIRST_NAME,
                "lastName": OrderData.LAST_NAME,
                "address": OrderData.LAST_NAME,
                "metroStation": OrderData.METRO_STATION,
                "phone": OrderData.METRO_STATION,
                "rentTime": OrderData.RENT_TIME,
                "deliveryDate": OrderData.DELIVERY_DATE,
                "comment": OrderData.COMMENT,
                "color": color
            }
        with allure.step('Отправка POST-запроса на /api/v1/orders'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.ORDER_CREATE}',json=payload)
        with allure.step('Проверка кода ответа'):    
            assert response.status_code == 201
        with allure.step('Проверка тела ответа'):
            assert "track" in response.json()
        