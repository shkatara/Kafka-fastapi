from fastapi import FastAPI,status
from uvicorn import run
from producer import produce_message
app = FastAPI()


@app.get("/produce",status_code=status.HTTP_200_OK)
def produce():
    message = produce_message()
    return {"message": "Sent Successful"} if message == None else {"error": "Sending Failed"}

if __name__ == "__main__":
   run("main:app", host="127.0.0.1", port=8000, reload=True,log_level="info")