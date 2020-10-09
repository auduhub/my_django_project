from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    # path('logout/',views.logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout')

]