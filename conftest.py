import pytest
import requests
import config
import data


@pytest.fixture
def courier():
    # создать курьера
    courier_data = data.register_new_courier_and_return_login_password()
    # логин, получаем ID курьера
    courier_id = data.login_courier(courier_data[0], courier_data[1])
    
    # отдаём тесту список с данными курьера
    yield courier_data 

    # удаляем курьера после теста
    requests.delete(f'{config.BASE_URL}{config.DELETE_COURIER}{courier_id}')
    