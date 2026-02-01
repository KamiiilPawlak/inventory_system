from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    sku: str
    price: float = Field(gt=0, description="Price must be greater than zero")
    quantity: int = Field(ge=0)
    min_stock_level: int = 5


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    from_attributes = True