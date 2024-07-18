from django.contrib.auth import views as auth_views
from django.urls import path

from users import views
from .views import CustomPasswordResetView

app_name = 'user_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('user/list/a/', views.UserListView.as_view(), name='list'),
    path('user/create/a/', views.UserCreateView.as_view(), name='create'),
    path('user/update/<int:pk>/a/', views.UserUpdateView.as_view(), name='update'),
    path('user/delete/<int:pk>/a/', views.UserDeleteView.as_view(), name='delete'),
    path('user/register/c/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('user/profile/<int:pk>/c/', views.UserProfile.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='user_app:home'), name='logout'),

        path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
