from django.urls import path
from .views import ArticleAPIVIEW, ArticleDetails

urlpatterns = [
    path('article/', ArticleAPIVIEW.as_view()),
    path('article_detail/<int:id>', ArticleDetails.as_view())
]