from django.urls import path

from . import views

app_name = 'image_process'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name="upload"),
    path('view/', views.view_image, name="view"),
    path('browse/', views.ImageListView.as_view(), name="browse"),

]
