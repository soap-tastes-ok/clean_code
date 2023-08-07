

---
ChatGPT Web App: Architecture
---

```mermaid

graph LR
subgraph VPC
    subgraph Public subnet
        A[React client] --> B[ELB] --> C[Flask server]
    end
    subgraph Private subnet
        D[SQLite server] --> C
    end
    E[User authentication] --> B
end
subgraph Internet
    F[User] --> A
end
subgraph AWS
    G[S3 bucket]
end
C --> G

```