from enum import Enum

from pydantic import BaseModel


class SourceEnum(str, Enum):
    RBK = 'rbk'
    MEDUZA = 'meduza'
    OVD_INFO = 'ovd-info'
    RT = 'rt'


class SourceCreateSchema(BaseModel):
    title: SourceEnum
