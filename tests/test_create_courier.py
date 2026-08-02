import requests
from config import TextFail
from urls import Urls
import data
import allure
import pytest

class TestCreateCourier:

    @allure.title('Проверка успешного создания нового курьера')
    def test_succes_create_courier(self, clean_courier):
        with allure.step('Подготовка тестовых данных'):
            payload = {
                "login": data.generate_random_string(),
                "password": data.generate_random_string(),
                "firstName": data.generate_random_string()
            }
        with allure.step('Отправка POST-запроса на /api/v1/courier'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 201
        with allure.step('Проверка тела ответа'):
            assert response.json()["ok"] == True
        clean_courier['id'] = data.login_courier(payload["login"], payload["password"])


    @pytest.mark.xfail(reason='фактический message - Этот логин уже используется. Попробуйте другой.')
    @allure.title('Проверка попытки повторно зарегистрировать существующиего курьера')
    def test_registred_with_used_login(self, courier):
        with allure.step('Отправка POST-запроса на /api/v1/courier с логином существующего курьера'):
            payload = {
                "login": courier[0],
                "password": data.generate_random_string(),
                "firstName": data.generate_random_string()
            }
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 409
        with allure.step('Проверка текста ошибки'):
            assert response.json()["message"] == TextFail.MESSAGE409_COURIER


    @allure.title('Проверка попытки создания курьера без login')
    def test_no_login_registred(self):
        with allure.step('Подготовка тестовых данных'):
            payload = {
                "password": data.generate_random_string(),
                "firstName": data.generate_random_string()
            }
        with allure.step('Отправка POST-запроса на /api/v1/courier'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 400
        with allure.step('Проверка текста ошибки'):    
            assert response.json()["message"] == TextFail.MESSAGE400_COURIER


    @allure.title('Проверка попытки создания курьера без password')
    def test_no_password_registred(self):
        with allure.step('Подготовка тестовых данных'):
            payload = {
                "login": data.generate_random_string(),
                "firstName": data.generate_random_string()
            }
        with allure.step('Отправка POST-запроса на /api/v1/courier'):    
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 400
        with allure.step('Проверка текста ошибки'):
            assert response.json()["message"] == TextFail.MESSAGE400_COURIER
    

    @allure.title('Проверка создания нового курьера без firstName')
    def test_create_courier_no_first_name(self, clean_courier):
        with allure.step('Подготовка тестовых данных'):
            payload = {
                "login": data.generate_random_string(),
                "password": data.generate_random_string(),
            }
        with allure.step('Отправка POST-запроса на /api/v1/courier'):    
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 201
        with allure.step('Проверка тела ответа'):
            assert response.json()["ok"] == True
        clean_courier['id'] = data.login_courier(payload["login"], payload["password"])
        