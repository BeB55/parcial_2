from django.urls import path
from .views import registro, CustomLoginView, CustomLogoutView
from . import views

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
