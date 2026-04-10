from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def get_data(url: str, token: str, auth: str):
    return {
        "url": url,
        "message": "API working hai bhai 😎"
    }
