from django.urls import path
from . import views
from .views import ProductListCreateView, ProductDetailView,AllProductsListView,ProductDeleteView,ProductUpdateView

urlpatterns = [
    path('product/', ProductListCreateView.as_view(), name='Product-list-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='Product-detail'),
    path('product/all/', AllProductsListView.as_view(), name='all-Product-list'),  
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(http_method_names=['delete']), name='Product-delete'), 
    # path('product/delete/<int:pk>/', views.product_delete, name='Product-delete'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='Product-update'), 
]