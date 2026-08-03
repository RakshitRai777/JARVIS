from tools.tool_registry import ToolRegistry
from tools.applications.chrome_tool import ChromeTool


def test_tool_registration():

    registry = ToolRegistry()

    registry.register(
        ChromeTool()
    )

    assert registry.get("chrome") is not None


def test_unknown_tool():

    registry = ToolRegistry()

    assert registry.get("spotify") is None


def test_registry_count():

    registry = ToolRegistry()

    registry.register(
        ChromeTool()
    )

    assert len(registry.all()) == 1


def test_registry_clear():

    registry = ToolRegistry()

    registry.register(
        ChromeTool()
    )

    registry.clear()

    assert len(registry.all()) == 0