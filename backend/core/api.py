from ninja import Router, File, Form, UploadedFile, Query
from ninja.pagination import paginate, PageNumberPagination
from typing import List
from .models import Product, Category

from .schemas import ProductIn, ProductOut, ProductFilter, CategoryOut
from django.shortcuts import get_object_or_404

router = Router()

@router.get("/products", response=List[ProductOut])
@paginate(PageNumberPagination, page_size=10)
def list_products(request, filters: ProductFilter = Query(...)):
    qs = Product.objects.all()
    
    # Ninja automatically applies the filters defined in the schema!
    qs = filters.filter(qs)
    
    return qs

@router.get("/products/{product_id}", response=ProductOut)
def get_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product

# UPDATED ENDPOINT
@router.post("/products", response=ProductOut)
def create_product(request, payload: ProductIn = Form(...), image: UploadedFile = File(None)):
    # 1. Convert the Form payload to a dictionary
    data = payload.dict()
    
    # 2. Create the product (passing the image if it exists)
    product = Product.objects.create(**data, image=image)
    return product

@router.get("/categories", response=List[CategoryOut])
def list_categories(request):
    return Category.objects.all()