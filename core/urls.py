
from django.contrib import admin
from django.urls import path
from accounts.views import dashboard_view, login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', login_view), # This makes login the home page
]