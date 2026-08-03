from tools.applications.chrome_tool import ChromeTool


def test_chrome_tool():

    tool = ChromeTool()

    result = tool.execute(
        "open chrome"
    )

    assert result.success is True

    assert result.message == "Chrome tool executed."