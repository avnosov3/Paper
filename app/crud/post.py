from app.crud.base import CRUDBase
from app.models.post import Post


class CRUDPost(CRUDBase):
    pass


post_crud = CRUDPost(Post)
