import time

from ai.verification.verification_manager import VerificationManager
from ai.waiting.wait_condition import WaitCondition
from ai.waiting.wait_result import WaitResult


class WaitManager:
    """
    Waits until a verification condition becomes true.

    Responsibilities
    ----------------
    • Poll VerificationManager
    • Stop on success
    • Stop on timeout

    Future Responsibilities
    -----------------------
    • Adaptive polling
    • Cancellation
    • Multiple wait conditions
    """

    ############################################################

    def __init__(self):

        self.verification_manager = VerificationManager()

    ############################################################

    def wait_until(
        self,
        condition: WaitCondition,
    ) -> WaitResult:

        start = time.perf_counter()

        ########################################################

        while True:

            ####################################################
            # Verify
            ####################################################

            result = self.verification_manager.verify(

                condition.rule

            )

            ####################################################

            if result.success:

                return WaitResult(

                    success=True,

                    message=result.message,

                    elapsed_time=(
                        time.perf_counter()
                        - start
                    ),

                    data=result.data,

                )

            ####################################################
            # Timeout?
            ####################################################

            elapsed = (

                time.perf_counter()

                - start

            )

            if elapsed >= condition.timeout:

                return WaitResult(

                    success=False,

                    timed_out=True,

                    elapsed_time=elapsed,

                    error=(

                        f"Timed out waiting for "

                        f"{condition.rule}"

                    ),

                )

            ####################################################
            # Wait
            ####################################################

            time.sleep(

                condition.poll_interval

            )