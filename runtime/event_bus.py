from collections import defaultdict
from threading import Lock
from typing import Callable, Any


class EventBus:
    """
    Thread-safe publish/subscribe event system.
    """

    def __init__(self):
        self._subscribers = defaultdict(list)
        self._lock = Lock()

    def subscribe(self, event_name: str, callback: Callable[..., Any]):
        """
        Register a callback for an event.
        """
        with self._lock:
            if callback not in self._subscribers[event_name]:
                self._subscribers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable[..., Any]):
        """
        Remove callback from event.
        """
        with self._lock:
            if callback in self._subscribers[event_name]:
                self._subscribers[event_name].remove(callback)

    def publish(self, event_name: str, *args, **kwargs):
        """
        Publish an event to every subscriber.
        """
        with self._lock:
            callbacks = list(self._subscribers[event_name])

        for callback in callbacks:
            callback(*args, **kwargs)

    def clear(self):
        with self._lock:
            self._subscribers.clear()

    def subscribers(self, event_name: str):
        with self._lock:
            return list(self._subscribers[event_name])