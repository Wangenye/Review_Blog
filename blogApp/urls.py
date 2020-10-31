from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', views.adminlogin, name="admin_login"),
    # path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/',views.adminlogin,name='login_url'),
    path('register/',views.AdminRegister,name='admin_register'),
    # path('logout/',LogoutView.as_view(),name='logout'),
]