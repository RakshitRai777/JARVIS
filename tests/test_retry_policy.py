from ai.execution.retry_policy import RetryPolicy


def main():

    ############################################################
    # Default Policy
    ############################################################

    print("=" * 60)
    print("DEFAULT POLICY")
    print("=" * 60)

    policy = RetryPolicy()

    print("Enabled      :", policy.enabled)
    print("Max Attempts :", policy.max_attempts)
    print("Delay        :", policy.delay_seconds)

    ############################################################
    # Custom Policy
    ############################################################

    print()
    print("=" * 60)
    print("CUSTOM POLICY")
    print("=" * 60)

    custom = RetryPolicy(

        enabled=True,

        max_attempts=5,

        delay_seconds=2.5,

    )

    print("Enabled      :", custom.enabled)
    print("Max Attempts :", custom.max_attempts)
    print("Delay        :", custom.delay_seconds)

    ############################################################
    # Disabled Policy
    ############################################################

    print()
    print("=" * 60)
    print("DISABLED POLICY")
    print("=" * 60)

    disabled = RetryPolicy(

        enabled=False,

        max_attempts=1,

        delay_seconds=0,

    )

    print("Enabled      :", disabled.enabled)
    print("Max Attempts :", disabled.max_attempts)
    print("Delay        :", disabled.delay_seconds)


if __name__ == "__main__":

    main()