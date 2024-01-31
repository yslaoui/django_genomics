from django.urls import include, path
from . import views
from . import api

urlpatterns = [
    path('', views.GeneList.as_view(), name='index'),
    path('gene/<int:pk>', views.GeneDetail.as_view(), name='gene'),
    path('list/<str:type>', views.GeneList.as_view(), name = 'list'),
    path('poslist', views.GeneList.as_view(), name = 'poslist'),
    path('delete/<int:pk>', views.GeneDelete.as_view(), name = 'delete'),
    path('update/<int:pk>', views.GeneUpdate.as_view(), name = 'delete'),
    path('create_ec', views.create_ec, name='create_ec'),
    path('create_gene', views.GeneCreate.as_view(), name='create_gene'),
    path('api/gene/<int:pk>', api.GeneDetail.as_view(), name='gene_detail_api'),
    path('api/genes', api.GeneList.as_view(), name='gene_list_api'), 
    path('api/ecs', api.EcList.as_view(), name='ec_list_api'), 
    path('api/ec/<int:pk>', api.EcDetail.as_view(), name='ec_detail_api'),
    path('api/list/<str:type>', api.GeneListType.as_view(), name='ec_detail_api'),
    path('app/', views.spa, name = "spa"), 
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout')


]
