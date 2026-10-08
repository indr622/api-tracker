import uvicorn


def main() -> None:
    uvicorn.run("api_tracker.main:app", host="127.0.0.1", port=8000, reload=True)
