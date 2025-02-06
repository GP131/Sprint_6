# Sprint_6 QA Practicum

UI-тестирование с Page Object Model и Allure сервиса "Яндекс.Самокат"

## Тестовые сценарии

1. Выпадающий список в разделе «Вопросы о важном»
2. Заказ самоката (весь флоу позитивного сценария с двумя наборами данных через две точки входа: кнопка «Заказать»
   вверху страницы и внизу)

## Тестовый Фреймворк

* pytest / selenium / allure

### Установить зависимости:

> pip install -r requirements.txt

### Запустить все тесты:

> $env:PYTHONPATH = "."
> pytest -v

### Посмотреть отчёт в браузере:

Запуск тестов с генерацией от allure
> $env:PYTHONPATH = "."
> pytest -v --alluredir=allure_results

Просмотр тестов в браузере
> allure serve allure_results
