import requests
from urls import Urls
import allure

class TestOrdersList:
    
    @allure.title('Проверка получения списка заказов')
    def test_get_orders_list(self):
        with allure.step('Отправка GET-запроса на /api/v1/orders'):
            response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_LIST}')
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 200
        with allure.step('Проверка что тело ответа содержит заказы - orders'):    
            assert "orders" in response.json()
        with allure.step('Проверка что orders - список'):    
            assert isinstance(response.json()["orders"], list)
