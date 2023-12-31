# Код для виджета «Операции по счетам»

<aside>
👨🏻‍💻 IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. Вам доверили реализовать алгоритм, который на бэкенде будет готовить данные для отображения в новом виджете.
</aside>

## Задача

Реализуйте функцию, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:

<дата перевода> <описание перевода>

<откуда> -> <куда>

<сумма перевода> <валюта>

### Требования

- Последние 5 выполненных (EXECUTED) операций выведены на экран.
- Операции разделены пустой строкой.
- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
- Сверху списка находятся самые последние операции (по дате).
- Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
- Номер счета замаскирован и не отображается целиком в формате  **XXXX 
(видны только последние 4 цифры номера счета).

-------------------------------------------------------------------------------

### Состав проекта:
1. Данные для проекта находятся в папке "**data**";
2. Функции для работы программы находятся в папке "**src**" в файле "**utils.py**";
3. Исполняемая функция находится в папке "**src**" в файле "**main.py**";
4. Функции для тестирования находятся в папке "**tests**" в файле "**test_utils.py**";
5. Тесты написаны на **pytest**;
6. Информация о требованиях проекта находится в файле "**requirements.txt**".

--------------------------------------------------------------------------

© Виталий Кириллов, 28.09.2023 г.