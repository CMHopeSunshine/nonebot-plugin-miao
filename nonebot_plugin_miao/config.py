from typing import List, Literal

from nonebot import get_driver
from pydantic import BaseModel, Field, Extra

driver = get_driver()


class Config(BaseModel, extra=Extra.ignore):
    miao_words: List[str] = ['喵', '旺']
    miao_probability: float = Field(0.5, ge=0, le=1)
    miao_position: Literal['start', 'end', 'random'] = 'end'
    miao_count: int = 1


config = Config.parse_obj(driver.config.dict())
