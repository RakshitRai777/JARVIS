from dataclasses import dataclass, field
from datetime import datetime
import threading


@dataclass
class RuntimeState:
    """
    Stores the live state of the JARVIS runtime.
    Every subsystem reads and updates this object.
    """

    # ===== Runtime =====
    is_running: bool = False
    is_initialized: bool = False
    shutdown_requested: bool = False

    # ===== AI State =====
    is_listening: bool = False
    is_thinking: bool = False
    is_speaking: bool = False

    # ===== System =====
    debug_mode: bool = False
    online: bool = True

    # ===== Metadata =====
    start_time: datetime | None = None
    current_user: str = "Rakshit"

    # ===== Thread Safety =====
    lock: threading.Lock = field(default_factory=threading.Lock)

    def start(self):
        with self.lock:
            self.is_running = True
            self.start_time = datetime.now()

    def stop(self):
        with self.lock:
            self.is_running = False
            self.shutdown_requested = True

    def initialize(self):
        with self.lock:
            self.is_initialized = True

    def listening(self, state: bool):
        with self.lock:
            self.is_listening = state

    def thinking(self, state: bool):
        with self.lock:
            self.is_thinking = state

    def speaking(self, state: bool):
        with self.lock:
            self.is_speaking = state