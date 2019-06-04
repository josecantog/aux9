from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('added_project/', views.added_project, name='added_project'),
	path('add_proyecto', views.add_proyecto, name='add_proyecto'),
	path('new_project/', views.new_project, name='new_project'),
	path('lista_proyectos/',views.lista_proyectos, name='lista_proyectos'),
	path('lista_estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
	path('new_ramo/', views.new_ramo, name='new_ramo'),
	path('added_ramo/', views.added_ramo, name='added_ramo'),
	path('add_ramo', views.add_ramo, name='add_ramo'),
	path('modificar_ramo', views.modificar_ramo, name='modificar_ramo'),
	path('new_user/', views.crear_usuario, name='new_user'),
	path('new_user/create', views.usuario_creado, name='create_user'),
	path('login', views.loginView, name='login'),
	path('auth', views.auth, name='auth'),
	path('logout', views.logoutView, name='logout'),
]

