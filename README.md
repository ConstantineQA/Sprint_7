# Sprint_7
## API тесты для sprint_7

### Основная информация о проекте
1. Автотесты написаны для учебного сервиса Яндекс Самокат (https://qa-scooter.education-services.ru/).
2. Документация API - https://qa-scooter.praktikum-services.ru/docs/ 
3. Основа для написания автотестов: pytest, selenium, requeqsts.
4. Команда для запуска: pytest -vv

### Перечень файлов

1. conftest.py - фикстуры
2. config.py - месседжи ошибок
3. urls.py - url, эндпоинты 
3. data.py - вспомогательные методы (создание курьера, логин, генерация рандомной строки), тестовые данные для заказа
4. requirmements.txt - зависимости
5. tests/test_login.py - тесты логина курьера 
6. tests/test_get_list_orders.py - тест получения списка заказов
7. tests/test_create_order.py - тесты оформления заказа
8. tests/test_create_courier.py - тесты регистрации нового курьера
9. allure-report/- отчет о тестировании

### Перечень тестов
**test_login.py**
1. test_succes_login - Проверка успешной авторизации существующим пользователем.
2. test_login_incorrect_password - Проверка авторизации существующим пользователем с некорректным паролем
3. test_login_incorrect_login - Проверка авторизации существующим пользователем с некорректным логином
4. test_login_without_login - Проверка обработки сценарии авторизации без логина
5. test_login_without_password - Проверка обработки сценарии авторизации без пароля
6. test_login_nonexistent_courier - Проверка авторизации незарегистрированным пользователем

**test_get_list_orders.py**
1. test_get_orders_list - Проверка получения списка заказов

**test_create_order.py**
1. test_create_order - Проверка создания заказа с самокатами разных цветов

**test_create_courier.py**
1. test_succes_create_courier - Проверка успешного создания нового курьера
2. test_registred_with_used_login - Проверка попытки повторно зарегистрировать существующиего курьера
3. test_no_login_registred - Проверка попытки создания курьера без логина
4. test_no_password_registred - Проверка попытки создания курьера без пароля
5. test_create_courier_no_first_name - Проверка попытки создания курьера без имени


### Запуск тестов

```bash
1. Запуск тестов с сохранением результатов
pytest --alluredir=allure-results
```
```bash
2. Генерация html отчета
allure generate allure-results --clean -o allure-report 
```
```bash
3. Проверка отчета локально
allure open allure-report 
```