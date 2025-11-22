from ninja import Schema, FilterSchema, Field
from typing import Optional
from decimal import Decimal

class CategoryOut(Schema):
    id: int
    name: str
    slug: str

class ProductOut(Schema):
    id: int
    name: str
    sku: str
    price: Decimal
    in_stock: bool
    image: str = None
    category: Optional[CategoryOut] = None  # <--- Nested Schema!

class ProductIn(Schema):
    name: str
    sku: str
    description: str = None
    price: Decimal
    in_stock: bool = True
    category_id: Optional[int] = None # <--- We accept ID for input

class ProductFilter(FilterSchema):
    # Search: Matches name OR sku (case-insensitive)
    search: Optional[str] = Field(None, q=['name__icontains', 'sku__icontains'])
    
    # Price filters: Map to price >= and price <=
    price_min: Optional[float] = Field(None, q='price__gte')
    price_max: Optional[float] = Field(None, q='price__lte')