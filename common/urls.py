from django.urls import path
from django.contrib.auth import views as auth_views
from common import views

app_name = 'common'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login1.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('security/', views.security, name='signup'),
    ]