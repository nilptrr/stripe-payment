# Тестовое задание - Stripe API
Создание платежной формы для товаров с помощью Stripe API

Описание задания: https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit#heading=h.njgtqq45axls

## Urls
- `/buy/<int:pk>/` - Stripe Session ID для оплаты товара
- `/item/<int:pk>/` - информация о товаре
- `/success/` - заказ успешно оплачен
- `/cancel/` - заказ отменен

## Установка
Установка зависимостей и активация виртуального окружения
```shell
$ poetry install
$ poetry shell
```

## Запуск
Применение миграций, заполнение БД тестовыми данными и запуск сервера
```
$/stripe_payment/manage.py migrate
$/stripe_payment/manage.py create_items
$/stripe_payment/manage.py runserver
```
