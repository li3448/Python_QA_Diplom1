## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

1. Клонировать репозиторий с проектом

2. Перейти в корень проекта

3. Настроить виртуальную среду (virtual environment):
   >  `$ python -m venv .venv

4. Запустить virtual environment:
   - Windows
   >  `$ .venv\Scripts\activate
   - MacOS/Linux:
   >  `$ source .venv/bin/activate

5. Установить зависимости:
   >  `$ pip install -r requirements.txt

6. Запуск тестов:
   >  `$ python -m pytest
   >  `$ python -m pytest --cov=praktikum --cov-report=html`
   > 