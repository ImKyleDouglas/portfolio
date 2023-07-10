from django.urls import path
from . import views

app_name = 'portfolio_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<str:project_title>/', views.project_view, name='project_page'),
    path('<str:project_title>/', views.project_with_link_view, name='project_with_link')
]

