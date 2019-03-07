from django.urls import path
from . import views

urlpatterns = [
	path('analytics', views.analytics, name = 'analytics'),
	path('', views.AddProject.as_view(), name='add_project')
]