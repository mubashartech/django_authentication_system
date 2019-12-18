from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
	path('', views.IndexView, name='index'),
	path('dashboard/', views.dashboardView, name='dashboard'),
	path('login/', LoginView.as_view(), name='login'),
	path('register/', views.RegisterView, name='register')
	#path('logout/')
]