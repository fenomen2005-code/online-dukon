from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('products/', views.product_list, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]