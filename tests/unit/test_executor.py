from ai.execution.execution_result import ExecutionResult


def test_execution_result():

    result = ExecutionResult(
        success=True,
        message="Hello"
    )

    assert result.success
    assert result.message == "Hello"