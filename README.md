# pucpr-devops

Repo da disciplina de DevOps (PUCPR).

## Rodar local

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- `GET /health` → `{"status": "ok"}`
- `GET /releases` → versão e ambiente

```bash
pytest
```
