from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_items, name='view_items'),
    path('add_item/', views.add_item, name='add_item'),
    path('check_price/<int:item_id>/', views.check_item_price, name='check_price'),

    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]
