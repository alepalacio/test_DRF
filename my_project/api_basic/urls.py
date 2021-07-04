from django.urls import path
"""
IMPORTING VIEWS FROM CLASS BASED VIEWS
"""
from .views import ArticleAPIView, SingleArticleAPIView
"""
IMPORTING VIEWS FROM FUNCTION BASED VIEWS.  NEED TO USE as_view()
"""
#from .views import article_list, article_single

urlpatterns = [
    
    path('', ArticleAPIView.as_view()),
    path('<int:pk>/', SingleArticleAPIView.as_view()),
    #path('', article_list),
    #path('<int:pk>/', article_single),
]