from fastapi import FastAPI
from uvicorn import run
from producer import produce_message
app = FastAPI()


@app.get("/produce")
def produce():
    return = produce_message()


if __name__ == "__main__":
   run("main:app", host="127.0.0.1", port=8000, reload=True,log_level="info")