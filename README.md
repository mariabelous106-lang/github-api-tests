![Run GitHub API Tests](https://github.com/mariabelous106-lang/github-api-tests/actions/workflows/tests.yml/badge.svg)

# GitHub API Tests

Автотесты для публичного GitHub API с использованием Pytest + Requests.

## Стек
- Python 3.14
- Pytest
- Requests
- JSON Schema
- Allure
- GitHub Actions

## Установка и запуск

```bash
git clone https://github.com/mariabelous106-lang/github-api-tests.git
cd github-api-tests
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Тесты

- `test_get_existing_user` — информация о существующем пользователе
- `test_get_nonexistent_user` — 404 для несуществующего пользователя
- `test_get_user_repos` — список репозиториев пользователя
- `test_get_user_with_invalid_username` — 404 для невалидного username
- `test_user_has_avatar` — проверка поля avatar_url

## Структура проекта

```
github-api-tests/
├── helpers/
│   ├── __init__.py
│   └── github_client.py
├── tests/
│   ├── __init__.py
│   └── test_users.py
├── conftest.py
├── requirements.txt
└── README.md
```

## CI/CD

Тесты запускаются автоматически через GitHub Actions при каждом пуше в `main`.