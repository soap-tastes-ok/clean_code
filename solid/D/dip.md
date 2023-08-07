
---
DIP: Same example from SRP
---
```mermaid

classDiagram
class ActivityLoader {
	load() dict
}
class EventIdentifier {
	identify(log: dict) int
}
class EventStreamer {
	stream(bytes)
}
class SystemMonitor {
	-_loader: ActivityLoader
	-_identifier: EventIdentifier
	-_streamer: EventStreamer
	run()
}


SystemMonitor ..o ActivityLoader: aggregates
SystemMonitor ..o EventIdentifier: aggregates
SystemMonitor ..o EventStreamer: aggregates

```


---
DIP: Bad example
---

Add a dependency to a concrete implementation
(the ExternalActor class).

```mermaid

classDiagram
class ActivityLoader {
	load() dict
}
class EventIdentifier {
	identify(log: dict) int
}
class EventStreamer {
	stream(bytes)
}
class SystemMonitor {
	-_loader: ActivityLoader
	-_identifier: EventIdentifier
	-_streamer: EventStreamer
	run()
}

class SystemLog {
	send(event)
}

SystemLog <.. SystemMonitor: depends on
SystemMonitor ..o ActivityLoader: aggregates
SystemMonitor ..o EventIdentifier: aggregates
SystemMonitor ..o EventStreamer: aggregates


```


---
DIP: Good example
---
Invert the dependency and make both
SystemMonitor & SystemLog to depend on an abstract class.

```mermaid


classDiagram
class ActivityLoader {
	load() dict
}
class EventIdentifier {
	identify(log: dict) int
}
class EventStreamer {
	stream(bytes)
}
class SystemMonitor {
	-_loader: ActivityLoader
	-_identifier: EventIdentifier
	-_streamer: EventStreamer
	run()
}

class DataTargetClient {
	<<abstract class>>
	+send(event: Event)
}


class SystemLog {
	send(event)
}

SystemLog --|> DataTargetClient: inherits

DataTargetClient <.. SystemMonitor: depends on
SystemMonitor ..o ActivityLoader: aggregates
SystemMonitor ..o EventIdentifier: aggregates
SystemMonitor ..o EventStreamer: aggregates

```

---
DIP:Good example
---
```mermaid


classDiagram
class ActivityLoader {
	load() dict
}
class EventIdentifier {
	identify(log: dict) int
}
class EventStreamer {
	stream(bytes)
}
class SystemMonitor {
	-_loader: ActivityLoader
	-_identifier: EventIdentifier
	-_streamer: EventStreamer
	run()
}

class DataTargetClient {
	<<abstract class>>
	+send(event: Event)
}


class SystemLog {
	send(event)
}

class Email {
	send(event)
}

class SqlServer {
	send(event)
}

class MyCustomDatabase {
	send(event)
}

SystemLog --|> DataTargetClient: inherits
Email --|> DataTargetClient: inherits
SqlServer --|> DataTargetClient: inherits
MyCustomDatabase --|> DataTargetClient: inherits

DataTargetClient <.. SystemMonitor: depends on
SystemMonitor ..o ActivityLoader: aggregates
SystemMonitor ..o EventIdentifier: aggregates
SystemMonitor ..o EventStreamer: aggregates

```
