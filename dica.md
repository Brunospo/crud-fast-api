# Padrão de desenvolvimento FastApi

Em projetos **FastAPI**, mesmo quando dizemos “MVC”, na prática usamos uma variação mais próxima de **MV* (Model–View–Router)**.
A pasta **schemas** não faz parte do MVC clássico — ela pertence ao padrão usado pelo FastAPI com **Pydantic** para validação/serialização de dados.

## 📌 Onde colocar a pasta `schemas`?

O padrão mais aceito na comunidade FastAPI é:

```bash
app/
│
├── api/
│   ├── v1/
│   │   └── routes.py
│   └── ...
│
├── core/
│
├── models/       <-- Modelos do ORM (SQLAlchemy)
│   └── user.py
│
├── schemas/      <-- Pydantic Schemas (entrada/saída da API)
│   └── user.py
│
├── services/     <-- Lógica de negócio
│
├── repositories/ <-- Acesso a dados
│
└── main.py
```

### ✔️ Justificativa

* **Models** = representam tabelas e entidades no banco (SQLAlchemy).
* **Schemas** = representam estruturas de dados para requests/responses (Pydantic).
* Como são camadas diferentes, devem ficar em pastas separadas.
* O diretório `schemas/` fica no mesmo nível que `models/`, `services/` e `api/`.

### 📌 Dica adicional

Se o projeto crescer, você pode organizar por **módulos/recursos**, por exemplo:

```bash
app/
│
└── users/
    ├── models.py
    ├── schemas.py
    ├── routes.py
    └── service.py
```

Essa estrutura modular também é bastante utilizada.

---

Se quiser, posso montar para você um esqueleto completo de projeto FastAPI em MVC modularizado.
