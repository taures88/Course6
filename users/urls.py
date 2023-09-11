from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, verification_user, password_recovery, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),  # Авторизация
    path('logout/', LogoutView.as_view(), name='logout'),  # Выход
    path('register/', RegisterView.as_view(), name='register'),  # Регистрация
    path('success_register/<str:register_uuid>/', verification_user, name='success_register'),  # Верификация
    path('password_recovery', password_recovery, name='password_recovery'),  # Восстановление пароля и электронной почты
    path('profile/', UserUpdateView.as_view(), name='profile'),  # Изменение
]
