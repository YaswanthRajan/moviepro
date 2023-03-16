from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.demo, name='mo'),
    path('movie/<int:id>/', views.detail, name="detail"),
    path('gg', views.add, name='aa'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('list', views.movielistview.as_view(), name="list"),
    path('cbvdetail/<int:pk>/', views.moviedetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.movieupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.moviedeleteview.as_view(), name="cbvdelete")
]
