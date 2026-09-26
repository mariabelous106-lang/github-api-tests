import requests


class GitHubClient:
    """Клиент для работы с GitHub API."""

    BASE_URL = "https://api.github.com"
    HEADERS = {"Accept": "application/vnd.github+json", "User-Agent": "qa-test-client"}

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def get_user(self, username: str):
        """Получает информацию о пользователе."""
        url = f"{self.BASE_URL}/users/{username}"
        return self.session.get(url)

    def get_user_repos(self, username: str):
        """Получает список репозиториев пользователя."""
        url = f"{self.BASE_URL}/users/{username}/repos"
        return self.session.get(url)

    def get_nonexistent_user(self, username: str):
        """Проверяет несуществующего пользователя (для негативных тестов)."""
        url = f"{self.BASE_URL}/users/{username}"
        return self.session.get(url)
