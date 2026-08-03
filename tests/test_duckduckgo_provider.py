from ai.web.providers.duckduckgo_provider import DuckDuckGoProvider


def test_provider_creation():

    provider = DuckDuckGoProvider()

    assert provider is not None

    assert provider.max_results == 5