from django.urls import path,include
from .views import home,TodosMVS

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("list", TodosMVS)

urlpatterns = [
    path('', home ),
    path("", include(router.urls))
]