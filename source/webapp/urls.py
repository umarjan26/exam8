from django.urls import path

from webapp.views.products import ProductIndex, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndex.as_view(), name='product_index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete')
]
