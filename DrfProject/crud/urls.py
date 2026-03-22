from django.urls import path,include
from .views import CrudApiView

'''If you are using viewset then to convert viewset into api urls we use 
router'''
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('view',CrudApiView)

urlpatterns = [
    path('',include(router.urls))
     
]
