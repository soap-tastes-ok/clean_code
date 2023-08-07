
---
Follows LSP
---
Sub-classes extends super-class.
All sub-classes have the same method of the super-class,
and they can take place of the super-class.

```mermaid

classDiagram

class Type {
    +method_0()
}

class SubType1 {
    +method_0()
    +method_1()
}

class SubType2 {
    +method_0()
    +method_2()
}

class SubType3 {
    +method_0()
    +method_3()
}

Client --> Type: uses
Type <|-- SubType1: Inherits
Type <|-- SubType2: Inherits
Type <|-- SubType3: Inherits
```

---
Violates LSP
---
None of the sub-classes can take place of the super-class.
This kind of design tells you your abstraction is wrong.
```mermaid

classDiagram

class Type {
    +method_0()
    +method_1()
    +method_2()
    +method_3()
}


class SubType1 {
    +method_1()
}

class SubType2 {
    +method_2()
}

class SubType3 {
    +method_3()
}

Client --> Type: uses
Type <|-- SubType1: Inherits
Type <|-- SubType2: Inherits
Type <|-- SubType3: Inherits
```


---
Violates LSP (example 2)
---
All sub-classes have the same method,
but have different arguments and returns.
This also violates LSP as sub-classes
can't take place of the super-class.

```mermaid

classDiagram

class Type {
    +method_0(a: list) bool
}


class SubType1 {
    +method_0(a) int
}

class SubType2 {
    +method_0(a: dict) bool
}

class SubType3 {
    +method_0(a, c) bool
}

Client --> Type: uses
Type <|-- SubType1: Inherits
Type <|-- SubType2: Inherits
Type <|-- SubType3: Inherits
```
