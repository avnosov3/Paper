from pydantic import BaseModel


class SubscriptionCreateSchema(BaseModel):
    title: str
