import requests
import config
import data
import allure
import pytest

class TestLogin:

    @allure.title('Тест успешного логина существующим пользователем')
    def test_succes_login(self, courier):     
        payload = {
            "login" : courier[0],
            "password" : courier[1]
        }
        response = requests.post(f'{config.BASE_URL}{config.COURIER_LOGIN}', data=payload)
        assert response.status_code == 200
        assert 'id' in response.json()


    @allure.title('Попытка логина существующим пользователем с некорректным паролем')
    def test_login_incorrect_password(self, courier):
        response = requests.post(f'{config.BASE_URL}{config.COURIER_LOGIN}', data={
            "login": courier[0],
            "password": data.generate_random_string()
        })
        assert response.status_code == 404
        assert response.json()["message"] == config.MESSAGE404_LOGIN


    @allure.title('Попытка логина существующим пользователем с некорректным логином')
    def test_login_incorrect_login(self, courier): 
        response = requests.post(f'{config.BASE_URL}{config.COURIER_LOGIN}', data={
            "login": data.generate_random_string(),
            "password": courier[1]
        })
        assert response.status_code == 404
        assert response.json()["message"] == config.MESSAGE404_LOGIN


    @allure.title('Попытка авторизации без логина')
    def test_login_without_login(self, courier):
        response = requests.post(f'{config.BASE_URL}{config.COURIER_LOGIN}', data={
            'password':courier[1]
        })
        assert response.status_code == 400
        assert response.json()["message"] == config.MESSAGE400_LOGIN


    @pytest.mark.xfail(reason='тест падает по таймауту, баг API')
    @allure.title('Попытка авторизации без пароля')
    def test_login_without_password(self, courier):
        response = requests.post(f'{config.BASE_URL}{config.COURIER_LOGIN}', data={
            'login':courier[0]
        })
        assert response.status_code == 400
        assert response.json()["message"] == config.MESSAGE400_LOGIN


    @allure.title('Попытка авторизации несуществующим пользователем')
    def test_login_nonexistent_courier(self):
        payload = {
            "login": data.generate_random_string(),
            "password": data.generate_random_string()
        }
        response = requests.post(f'{config.BASE_URL}{config.COURIER_LOGIN}',data=payload)
        assert response.status_code == 404
        assert response.json()["message"] == config.MESSAGE404_LOGIN
        