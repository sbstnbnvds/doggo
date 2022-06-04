from . import views
from django.urls import path

urlpatterns = [
	path('', views.home, name="home"),
	path('index', views.index, name="index"),
	path('ob/w', views.by_weight, name="by_weight"),
	path('ob/b', views.by_breed, name="by_breed"),

]