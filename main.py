from fastapi import FastAPI
from core import ALLUX_CORE_ONTOLOGY

app = FastAPI(title="Allux.ai", version="1.0")

@app.get("/")
def root():
    return {"status": "Allux online"}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/ontology")
def ontology():
    return ALLUX_CORE_ONTOLOGY
