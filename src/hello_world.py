from pydantic import BaseModel


class HelloWorldMessage(BaseModel):
    message: str


async def get_hello_msg() -> HelloWorldMessage:
    return HelloWorldMessage(**{"message": "Hello!"})
