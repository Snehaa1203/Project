from .views import *
from django.urls import path
urlpatterns=[
	path('',list,name='list'),
	path('product/<int:id>',detail,name='detail'),
	path('login/',login,name='login'),
	path('register/',register,name='register'),
	path('logout/',logoutUser,name='logout'),
]