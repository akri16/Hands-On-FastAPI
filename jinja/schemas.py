from fastapi import Form
from pydantic import BaseModel


class AwesomeForm(BaseModel):
    username: str
    password: str

    @classmethod
    def asForm(
        cls,
        username: str = Form(...),
        password: str = Form(...)
    ):
        return cls(
            username=username,
            password=password
        )



