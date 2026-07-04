import requests
import data
import allure
import pytest
from config import TextFail
from urls import Urls

class TestLogin:

    @allure.title('Тест успешного логина существующим пользователем')
    def test_succes_login(self, courier):  
        with allure.step('Подготовка тестовых данных'):   
            payload = {
                "login" : courier[0],
                "password" : courier[1]
            }
        with allure.step('Отправка POST-запроса на /api/v1/courier/login'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 200
        with allure.step('Проверка наличия id  в теле ответа'):    
            assert 'id' in response.json()


    @allure.title('Попытка логина существующим пользователем с некорректным паролем')
    def test_login_incorrect_password(self, courier):
        with allure.step('Отправка POST-запроса на /api/v1/courier/login'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data={
                "login": courier[0],
                "password": data.generate_random_string()
            })
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 404
        with allure.step('Проверка текста ошибки в ответе'):
            assert response.json()["message"] == TextFail.MESSAGE404_LOGIN


    @allure.title('Попытка логина существующим пользователем с некорректным логином')
    def test_login_incorrect_login(self, courier): 
        with allure.step('Отправка POST-запроса на /api/v1/courier/login'):    
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data={
                "login": data.generate_random_string(),
                "password": courier[1]
            })
        with allure.step('Проверка кода ответа'):    
            assert response.status_code == 404
        with allure.step('Проверка текста ошибки в ответе'):    
            assert response.json()["message"] == TextFail.MESSAGE404_LOGIN


    @allure.title('Попытка авторизации без логина')
    def test_login_without_login(self, courier):
        with allure.step('Отправка POST-запроса на /api/v1/courier/login'): 
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data={
                'password':courier[1]
            })
        with allure.step('Проверка кода ответа'):    
            assert response.status_code == 400
        with allure.step('Проверка текста ошибки в ответе'):    
            assert response.json()["message"] == TextFail.MESSAGE400_LOGIN


    @pytest.mark.xfail(reason='тест падает по таймауту, баг API')
    @allure.title('Попытка авторизации без пароля')
    def test_login_without_password(self, courier):
        with allure.step('Отправка POST-запроса на /api/v1/courier/login'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data={
                'login':courier[0]
            })
        with allure.step('Проверка кода ответа'):    
            assert response.status_code == 400
        with allure.step('Проверка текста ошибки в ответе'):    
            assert response.json()["message"] == TextFail.MESSAGE400_LOGIN


    @allure.title('Попытка авторизации несуществующим пользователем')
    def test_login_nonexistent_courier(self):
        with allure.step('Подготовка тестовых данных'):
            payload = {
                "login": data.generate_random_string(),
                "password": data.generate_random_string()
            }
        with allure.step('Отправка POST-запроса на /api/v1/courier/login'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}',data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 404
        with allure.step('Проверка текста ошибки в ответе'):    
            assert response.json()["message"] == TextFail.MESSAGE404_LOGIN
        