from fastapi import FastAPI,status,Response
from uvicorn import run
from producer import produce_message
app = FastAPI()


@app.get("/produce",status_code=status.HTTP_200_OK)
def produce(status_code: Response):
    message = produce_message()
    if message == None:
        status_code.status_code = status.HTTP_200_OK
        return {"message": "Sent Successful"} 
    else:                 
        status_code.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"error": "Sending Failed"}

if __name__ == "__main__":
   run("main:app", host="127.0.0.1", port=8000, reload=True,log_level="info")