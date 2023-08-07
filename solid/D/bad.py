_ = """Example 1
Let's say we are creating an application that is
in charge of reading logs about activities from a source
(can be a database, csv, log file, etc),
identify event that happened, and send it to
an external database/system called "SystemLog".
"""


# ⭐️ New class
class Event:
    """Some action we want to send"""

    def serialize(self):
        pass


# ⭐️ New class
class SystemLog:
    def send(self, event: bytes):
        """Send event to SystemLog for further processing"""
        pass


class ActivityLoader:
    def load(self):
        """Get the events from a source"""
        pass


class EventIdentifier:
    def identify(self):
        """Identify event from activity logs"""
        pass


# ⭐️ New implementation
class EventStreamer:
    def __init__(self, target: SystemLog):
        self._target = target

    def stream(self, events: list[Event]) -> None:
        """Send the parsed events to an external agent"""
        for event in events:
            self._target.send(event.serialize())


class SystemMonitor:
    def __init__(
        self,
        loader: ActivityLoader,
        identifier: EventIdentifier,
        streamer: EventStreamer,
    ):
        self._loader = loader
        self._identifier = identifier
        self._streamer = streamer

    def run(self):
        event_data = self._loader.load()
        event = self._identifier(event_data)
        self._streamer(event)

