import requests
import config
import data
import allure
import pytest

class TestCreateCourier:

    @allure.title('Проверка успешного создания нового курьера')
    def test_succes_create_courier(self):
        payload = {
            "login": data.generate_random_string(),
            "password": data.generate_random_string(),
            "firstName": data.generate_random_string()
        }
        response = requests.post(f'{config.BASE_URL}{config.COURIER_CREATE}', data=payload)
        assert response.status_code == 201
        assert response.json()["ok"] == True


    @pytest.mark.xfail(reason='фактический message - Этот логин уже используется. Попробуйте другой.')
    @allure.title('Проверка попытки повторно зарегистрировать существующиего курьера')
    def test_registred_with_used_login(self, courier):
        payload = {
            "login": courier[0],
            "password": data.generate_random_string(),
            "firstName": data.generate_random_string()
            # "password": courier[1],
            # "firstName": courier[2]
        }
        response = requests.post(f'{config.BASE_URL}{config.COURIER_CREATE}', data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == config.MESSAGE409_COURIER


    @allure.title('Проверка попытки создания курьера без login')
    def test_no_login_registred(self):
        payload = {
            "password": data.generate_random_string(),
            "firstName": data.generate_random_string()
        }
        response = requests.post(f'{config.BASE_URL}{config.COURIER_CREATE}', data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == config.MESSAGE400_COURIER


    @allure.title('Проверка попытки создания курьера без password')
    def test_no_password_registred(self):
        payload = {
            "login": data.generate_random_string(),
            "firstName": data.generate_random_string()
        }
        response = requests.post(f'{config.BASE_URL}{config.COURIER_CREATE}', data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == config.MESSAGE400_COURIER
    

    @allure.title('Проверка создания нового курьера без firstName')
    def test_create_courier_no_first_name(self):

        payload = {
            "login": data.generate_random_string(),
            "password": data.generate_random_string(),
        }
        response = requests.post(f'{config.BASE_URL}{config.COURIER_CREATE}', data=payload)
        assert response.status_code == 201
        assert response.json()["ok"] == True
