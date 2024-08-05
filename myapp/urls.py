from django.urls import path
from . import views
# from .views import UserListView
from .views import user_create_view, user_detail_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', user_create_view, name='user-list-create'),
    path('users/<int:pk>/', user_detail_view, name='user-details'),
]
