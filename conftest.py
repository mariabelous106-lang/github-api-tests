import pytest
from helpers.github_client import GitHubClient


@pytest.fixture(scope="function")
def client():
    """Фикстура: создаёт клиент GitHub API для каждого теста."""
    return GitHubClient()
