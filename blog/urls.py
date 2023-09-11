from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDetailView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),  # Создание
    path('', BlogListView.as_view(), name='list'),  # Все статьи
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),  # Изменеие
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),  # Просмотр
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),  # Удаление
]
