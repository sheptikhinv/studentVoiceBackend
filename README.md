# StudentVoice (backend)
Реализация бэкенда на FastAPI + SQLAlchemy via alembic

## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение
3. ```pip install -r requirements``` для установки зависимостей
4. ```python main.py``` для запуска сервера
5. При ошибке типа "Run migrations" всё такое пишем ```alembic upgrade head```

При первом запуске будут запрошены необходимые для работы значения, после ввода они сохранятся в settings.ini