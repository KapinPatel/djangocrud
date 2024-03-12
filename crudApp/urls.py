from django.contrib import admin
from django.urls import path,include
from crudApp.views import CrudViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'companies',CrudViewSet)


urlpatterns = [
    path('',include(router.urls))
]