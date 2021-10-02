from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    amount: int
    description: Optional[str] = None
