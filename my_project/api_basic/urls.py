from django.urls import path
from .views import article_list, article_single

urlpatterns = [
    path('app/', article_list),
    path('app/<int:pk>', article_single)
]