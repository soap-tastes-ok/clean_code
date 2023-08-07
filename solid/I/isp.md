
---
ISP: Bad example
---
```mermaid
classDiagram

class EventParser {
    from_xml(data: str) dict
    from_json(data: str) dict
    from_html(data: str) dict
    from_csv(data: str) dict
    from_tsv(data: str) dict
    from_dat(data: str) dict
}

```

---
ISP: Bad example
---
If we have "SomeClass2" that only parses json,
it makes no sense it will have access to
the "from_xml" method.
It should not be able to see it's existance.
```mermaid
classDiagram

class EventParser {
    from_xml(data: str) dict
    from_json(data: str) dict
}

class SomeClass1 {
    <<Uses both Json and xml>>
}

class SomeClass2 {
    <<Uses json only>>
}

SomeClass1 --> EventParser: uses
SomeClass2 --> EventParser: uses

```

---
ISP: Good example
---
What is if we split the EventParser class into
smaller interfaces?
```mermaid
classDiagram

class EventParser {
    from_xml(data: str) dict
    from_json(data: str) dict
}

class XmlEventParser {
    from_xml(data: str) dict
}

class JsonEventParser {
    from_json(data: str) dict
}



EventParser --o XmlEventParser: aggregates
EventParser --o JsonEventParser: aggregates

```


---
ISP: Good example
---
Now, each "SomeClass1" and "SomeClass2" can have access
to its minimum interface that it requires!
```mermaid
classDiagram

class EventParser {
    from_xml(data: str) dict
    from_json(data: str) dict
}

class XmlEventParser {
    from_xml(data: str) dict
}

class JsonEventParser {
    from_json(data: str) dict
}

class SomeClass1 {
    <<Uses both Json and xml>>
}

class SomeClass2 {
    <<Uses json only>>
}

SomeClass1 ..> EventParser: uses
SomeClass2 ..> JsonEventParser: uses
EventParser --o XmlEventParser: aggregates
EventParser --o JsonEventParser: aggregates

```
