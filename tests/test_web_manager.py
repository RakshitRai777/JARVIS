from ai.web.web_manager import WebManager


def test_web_manager_creation():

    manager = WebManager()

    assert manager is not None

    assert manager.provider is not None