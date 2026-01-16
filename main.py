from fastapi import FastAPI

app = FastAPI(title="Allux.ai")

@app.get("/")
def root():
    return {"status": "Allux online"}

@app.get("/health")
def health():
    return {"ok": True}
