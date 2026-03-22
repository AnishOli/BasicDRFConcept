from django.urls import path
from .views import TestApiView
urlpatterns = [
    path('test',TestApiView.as_view()),
    path('test/update/<int:id>',TestApiView.as_view()),
    path('test/delete/<int:id>',TestApiView.as_view()),
    # path('product/',ProductApiView.as_view())
]