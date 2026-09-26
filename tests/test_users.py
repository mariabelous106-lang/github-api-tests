import allure
from jsonschema import validate

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "login": {"type": "string"},
        "id": {"type": "integer"},
        "html_url": {"type": "string"},
        "public_repos": {"type": "integer"},
    },
    "required": ["login", "id", "html_url"],
}


@allure.feature("GitHub Users")
@allure.story("Get existing user")
def test_get_existing_user(client):
    """Проверяем получение информации о существующем пользователе."""
    with allure.step("Отправляем GET-запрос на /users/octocat"):
        response = client.get_user("octocat")

    with allure.step("Проверяем статус-код 200"):
        assert (
            response.status_code == 200
        ), f"Ожидался 200, а пришёл {response.status_code}"

    with allure.step("Проверяем структуру ответа по JSON-схеме"):
        data = response.json()
        validate(instance=data, schema=USER_SCHEMA)


@allure.feature("GitHub Users")
@allure.story("Get nonexistent user")
def test_get_nonexistent_user(client):
    """Проверяем запрос несуществующего пользователя."""
    with allure.step("Отправляем GET-запрос на несуществующего пользователя"):
        response = client.get_user("nonexistent_user_xyz_99999")

    with allure.step("Проверяем статус-код 404"):
        assert (
            response.status_code == 404
        ), f"Ожидался 404, а пришёл {response.status_code}"


@allure.feature("GitHub Users")
@allure.story("Get user repos")
def test_get_user_repos(client):
    """Проверяем получение списка репозиториев пользователя."""
    with allure.step("Отправляем GET-запрос на /users/octocat/repos"):
        response = client.get_user_repos("octocat")

    with allure.step("Проверяем статус-код 200"):
        assert (
            response.status_code == 200
        ), f"Ожидался 200, а пришёл {response.status_code}"

    with allure.step("Проверяем, что ответ — непустой список"):
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0


@allure.feature("GitHub Users")
@allure.story("Get user with invalid username")
def test_get_user_with_invalid_username(client):
    """Проверяем запрос с некорректным username (спецсимволы)."""
    with allure.step("Отправляем GET-запрос с невалидным username"):
        response = client.get_user("invalid user!@#")

    with allure.step("Проверяем, что сервер вернул 404"):
        assert (
            response.status_code == 404
        ), f"Ожидался 404, а пришёл {response.status_code}"


@allure.feature("GitHub Users")
@allure.story("Check user avatar URL")
def test_user_has_avatar(client):
    """Проверяем, что у пользователя есть ссылка на аватар."""
    with allure.step("Получаем данные пользователя"):
        response = client.get_user("octocat")
        data = response.json()

    with allure.step("Проверяем, что поле avatar_url есть и не пустое"):
        assert "avatar_url" in data
        assert data["avatar_url"].startswith("https://")
