from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gene/<int:pk>', views.gene, name='gene'),
    path('list/<str:type>', views.list, name = 'list'),
    path('poslist', views.poslist, name = 'poslist'),
    path('delete/<int:pk>', views.delete, name = 'delete'),
    path('create_ec', views.create_ec, name='create_ec'),
    path('create_gene', views.create_gene, name='create_gene')
]
