from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('public/', views.public_items, name='public_items'),
    path('private/', views.private_items, name='private_items'),
    # path('manage/', views.manage_stock, name='manage_stock'),
    path('public/chart/', views.public_chart, name='public_chart'),
    path('private/chart/', views.private_chart, name='private_chart'),
    path('private/chart/factory/<str:factory_name>/', views.factory_chart, name='factory_chart'),
    path('backend/', views.backend, name='backend'),
    path('update_stock/<int:item_id>/', views.update_stock, name='update_stock'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update_stock/private/<int:item_id>/', views.update_private_stock, name='update_private_stock'),
    path('delete_item/private/<int:item_id>/', views.delete_private_item, name='delete_private_item'),
]

