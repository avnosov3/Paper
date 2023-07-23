from uuid import UUID

from pydantic import BaseModel


class DigestCreateSchema(BaseModel):
    digest_id: UUID
