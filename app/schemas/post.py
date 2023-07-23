from pydantic import BaseModel


class PostResponseSchema(BaseModel):
    text: str
    likes: int
