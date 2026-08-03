from ai.brain.brain import Brain


def test_brain_creation():

    brain = Brain()

    assert brain is not None

    assert brain.conversations is not None

    assert brain.context_builder is not None

    assert brain.planner is not None

    assert brain.executor is not None