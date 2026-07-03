#url сервиса
BASE_URL = 'https://qa-scooter.praktikum-services.ru'

#Эндпоинты
#создать курьера
COURIER_CREATE = '/api/v1/courier'
#логин
COURIER_LOGIN = '/api/v1/courier/login'
#создать заказ
ORDER_CREATE = '/api/v1/orders'
#получить список заказов
ORDERS_LIST = '/api/v1/orders'
#удалить курьера
DELETE_COURIER ='/api/v1/courier/'

#Текст ошибок
#создание курьера
MESSAGE400_COURIER = 'Недостаточно данных для создания учетной записи'
MESSAGE409_COURIER='Этот логин уже используется'
#Логин
MESSAGE404_LOGIN = 'Учетная запись не найдена'
MESSAGE400_LOGIN = 'Недостаточно данных для входа'
