from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from core.api import router as core_router
from django.conf import settings             # <--- Import
from django.conf.urls.static import static   # <--- Import


api = NinjaAPI()
api.add_router("/", core_router) # Adds /products endpoints

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)