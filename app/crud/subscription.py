from app.crud.base import CRUDBase
from app.models.subscription import Subscription


class CRUDSubscription(CRUDBase):
    pass


subscription_crud = CRUDSubscription(Subscription)
