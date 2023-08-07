_ = """Example 1
Let's say we are creating an application that is
in charge of reading info about events from a source
(can be a database, csv, log file, etc),
decide action to take, and send it to
another external software.
"""


class ActivityLoader:
    def load(self):
        """Load activity logs from a source"""
        pass


class EventIdentifier:
    def identify(self):
        """Identify event from activity logs"""
        pass


class EventStreamer:
    def stream(self):
        """Send the parsed events to an external agent"""
        pass


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
        activity_data = self._loader.load()
        events = self._identifier(activity_data)
        self._streamer(events)

