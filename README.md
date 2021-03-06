# Сервис для хранения данных о пользователях
>Модели созданы на основе спецификации API. Из различий: Во все модели добавлено поле login, которое служит для идентификации пользователей.  

>Админы не могут менять поле "id" у пользователей, но могут менять поле "login". 
Это сделано для того, чтобы не нарушалась связь между объектами, если появятся дополнительные связные модели.  

>Также для упрощения поиска пользователей было добавлено 2 фильтра: фильтр сортировки (через параметр ordering) и фильтр поиска (через параметр search).  

>Пользователям была добавлена возможность входить в аккаунт не только по логину, но и по почте (просто дополнительная функция, которая упростит авторизацию пользователей).  

>Для админов была добавлена возможность управлять таблицей городов через patch: private/cities/ и private/cities/{pk}.  

>Также в модель пользователя было добавлено 2 поля: 1) Дата создания - очень полезное поле, чтобы знать когда пользователь был создан. 2) Дата последнего входа - также полезное поле, позволяющее следить за активностью пользователей.
## Используемые библиотеки:
>Django, django-rest-framework, django-filter  

>Также используется библиотека django-debug-toolbar для вывода отладочной панели инструментов  

>Также подключен swagger с использованием библиотеки drf-yasg
## Возможные ошибки:
>404 - когда задан неверный адрес или не вышло получить объект модели  

>403 - когда у пользователя не хватает прав для доступа к странице  

>400 - когда происходит ошибка при валидации полей  

>Не разобрался как вывести ошибку 401 в drf, используя встроенный механизм проверки аутентификации  

>Не понял когда нужно выводить ошибку 422, если при валидации json, то чтобы это реализовать придётся дополнять каждый метод, который работает с валидацией и менять поведение, чтобы выводить нужный код ошибки (не считаю, что это нужно, т.к. информация об ошибка всеравно выводится пользователю).  
## Тесты:
>Тесты написаны только для тестирования базового функционала api.