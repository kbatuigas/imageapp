from django.urls import path

from . import views

app_name = 'image_process'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name="upload"),
    path('view/', views.view_image, name="view"),
    path('blurred/', views.view_blurred, name="blurred"),
    path('bin/', views.view_binary, name="bin"),
    path('gbin/', views.view_gbin, name="gbin"),
    path('browse/', views.ImageListView.as_view(), name="browse"),

]
