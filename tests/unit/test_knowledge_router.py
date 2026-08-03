from ai.knowledge.knowledge_router import KnowledgeRouter
from ai.knowledge.knowledge_source import KnowledgeSource


def test_memory_route():

    router = KnowledgeRouter()

    result = router.route(
        "What is my favourite colour?"
    )

    assert result.source == KnowledgeSource.MEMORY


def test_web_route():

    router = KnowledgeRouter()

    result = router.route(
        "Who is the Chief Minister of Uttarakhand?"
    )

    assert result.source == KnowledgeSource.WEB


def test_weather_route():

    router = KnowledgeRouter()

    result = router.route(
        "What's the weather today?"
    )

    assert result.source == KnowledgeSource.WEB


def test_llm_route():

    router = KnowledgeRouter()

    result = router.route(
        "Tell me a joke."
    )

    assert result.source == KnowledgeSource.LLM