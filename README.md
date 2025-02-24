# FastAPI Project

Этот проект представляет собой веб-приложение, разработанное с использованием [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/) и [uvicorn](https://www.uvicorn.org/). В нём реализована базовая архитектура с использованием паттерна слойной архитектуры, что позволяет разделить слои моделей, DTO (Data Transfer Objects), репозиториев, сервисов и представлений.

## Структура проекта

- **Конфигурация и запуск:**
  - Файл [src/base/main.py](src/base/main.py) инициализирует приложение, создаёт таблицы в БД и импортирует маршруты.
  - Файл [src/base/engine.py](src/base/engine.py) содержит настройку подключения к базе данных.
  - Конфигурация запуска для отладки определена в [.vscode/launch.json](.vscode/launch.json).

- **Слои приложения:**
  - **Модели**: Определены в [src/apps/accounts/models/user.py](src/apps/accounts/models/user.py).
  - **DTO**: Описаны в [src/apps/accounts/dtos/dto.py](src/apps/accounts/dtos/dto.py).
  - **Репозитории**: Логика работы с базой данных реализована в [src/apps/accounts/repositories/users.py](src/apps/accounts/repositories/users.py) с базовой логикой в [src/base/abstracts/repositories.py](src/base/abstracts/repositories.py).
  - **Сервисы**: Содержат бизнес-логику, например, [src/apps/accounts/services/users.py](src/apps/accounts/services/users.py).
  - **Представления (views)**: Определяют маршруты API. Пример – [src/apps/accounts/views/users.py](src/apps/accounts/views/users.py) с маршрутом для регистрации пользователя.

- **Конфигурация:**
  - Параметры подключения к БД загружаются из переменных окружения (см. [.env.example](.env.example)) через [src/configs/settings/base.py](src/configs/settings/base.py).

## Как запустить

### Установка зависимостей

Установите зависимости, указанные в [requirements.txt](requirements.txt):

```sh
pip install -r requirements.txt

Настройка переменных окружения
Создайте файл .env на основании .env.example и задайте переменную SQLALCHEMY_DATABASE_URL. Пример:

Запуск сервера
Вы можете запустить приложение с помощью uvicorn:
- ** uvicorn src.base.main:app --reload **