from pydantic import BaseModel


class PostCreateSchema(BaseModel):
    text: str
    likes: int
