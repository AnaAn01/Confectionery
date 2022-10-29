from django.urls import path
from .views import (
    get_data,
    remove_from_cart,
    add_to_cart,
    # ProductView,
    CatalogView
)

app_name = 'products'
urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    # path('product/<pk>/', ProductView.as_view(), name='product'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('get_data/', get_data, name='get_data'),
]