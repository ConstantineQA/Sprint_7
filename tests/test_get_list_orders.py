import requests
import config
import allure

class TestOrdersList:
    
    @allure.title('Проверка получения списка заказов')
    def test_get_orders_list(self):
        response = requests.get(
            f'{config.BASE_URL}{config.ORDERS_LIST}'
        )
        
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
