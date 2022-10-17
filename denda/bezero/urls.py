from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bezero/', views.bezero, name='bezero'),
    path('produktuak/', views.produktuak, name='produktuak'),
    path('add/', views.add, name='add'),
    path('add/addbezero/', views.addbezero, name='addbezero'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updatebezero/<int:id>', views.updatebezero, name='updatebezero'),
]