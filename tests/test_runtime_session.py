from ai.runtime.runtime import Runtime


def main():

    runtime = Runtime()

    print("=" * 60)
    print("SESSION 1")
    print("=" * 60)

    session1 = runtime.runtime_session

    print("Session ID :", session1.session_id)
    print("Active     :", session1.active)
    print("Started    :", session1.started_at)
    print("Ended      :", session1.ended_at)
    print("History    :", len(session1.history))

    ############################################################

    runtime.reset()

    ############################################################

    print()
    print("=" * 60)
    print("SESSION 2")
    print("=" * 60)

    session2 = runtime.runtime_session

    print("Session ID :", session2.session_id)
    print("Active     :", session2.active)
    print("Started    :", session2.started_at)
    print("Ended      :", session2.ended_at)
    print("History    :", len(session2.history))

    ############################################################

    print()
    print("=" * 60)
    print("COMPARISON")
    print("=" * 60)

    print("Different IDs :", session1.session_id != session2.session_id)
    print("Session1 Ended:", session1.ended_at is not None)
    print("Session2 Active:", session2.active)


if __name__ == "__main__":
    main()