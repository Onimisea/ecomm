from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),


    path('categories/', views.categories_list, name='categories_list'),
    
    path('category/<slug:category_slug>/<slug:subcategory_slug>/', views.subcategory_list, name='subcategory_list'),
    
    path('<slug:slug>', views.product_detail, name='product_detail'),
]
