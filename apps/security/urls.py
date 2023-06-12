from django.urls import path
from knox import views as knox_views

from .views import CreateUserView, LoginView, ManageUserView

urlpatterns = [
    path("auth/create/", CreateUserView.as_view(), name="create"),
    path('auth/profile/', ManageUserView.as_view(), name='profile'),
    path('auth/login/', LoginView.as_view(), name='knox_login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    
]
