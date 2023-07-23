from app.crud.base import CRUDBase
from app.models.digest import Digest


class CRUDDigest(CRUDBase):
    pass


digest_crud = CRUDDigest(Digest)
