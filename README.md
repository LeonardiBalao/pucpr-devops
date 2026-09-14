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

## Docker

```bash
docker build -t pucpr-devops .
docker run -d --name pucpr-devops -p 8000:8000 pucpr-devops
```

## Observacao

Projeto da disciplina de DevOps (PUCPR).
