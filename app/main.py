from fastapi import FastAPI

app = FastAPI(title="pucpr-devops", version="1.0.0")

APP_VERSION = "1.0.0"
AMBIENTE = "producao"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/releases")
def releases():
    return {"app": "pucpr-devops", "versao": APP_VERSION, "ambiente": AMBIENTE}
