from app.crud.base import CRUDBase
from app.models.source import Source


class CRUDSource(CRUDBase):
    pass


source_crud = CRUDSource(Source)
