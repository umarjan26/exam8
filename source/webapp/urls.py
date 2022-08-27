from django.urls import path

from webapp.views.products import ProductIndex, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView
from webapp.views.reviews import ReviewCreateView, ReviewUpdateView, ReviewDeleteView, ReviewView, ReviewModerUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndex.as_view(), name='product_index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/review/add/', ReviewCreateView.as_view(), name='review_create'),
    path('product/<int:pk>/review/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('product/<int:pk>/review/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('reviews/', ReviewView.as_view(), name='review_index'),
    path('product/<int:pk>/review/update/moder', ReviewModerUpdateView.as_view(), name='review_update_moder'),
]
