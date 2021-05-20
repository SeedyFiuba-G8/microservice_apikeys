import os
import uvicorn
from fastapi import FastAPI
from hello_world import get_hello_msg, HelloWorldMessage

app = FastAPI()


@app.get("/", response_model=HelloWorldMessage)
async def home():
    return await get_hello_msg()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=os.environ['PORT'])
