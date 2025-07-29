from django.urls import path
from .views import NewsViewSet

urlpatterns = [
    path("create/", NewsViewSet.as_view({"post": "create"}), name="news-create"),
    path("", NewsViewSet.as_view({"get": "list"}), name="news-list"),
    path("<int:pk>/comments/", NewsViewSet.as_view({"get": "comments_by_news"}), name="news-comments"),
    path("<int:pk>/add-comment/", NewsViewSet.as_view({"post": "add_comment"}), name="news-add-comment"),
]
