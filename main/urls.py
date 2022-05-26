from django.urls import path

from .views import *

urlpatterns = [
    path('lists/', ProductAPIView.as_view()),
    path('<int:pk>/', RetrieveProductView.as_view()),
    path('delete/<int:pk>/', DestroyProductView.as_view()),
    path('update/<int:pk>/', UpdateProductView.as_view()),
    path('create/', CreateProductView.as_view()),

]