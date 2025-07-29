from news.models import NewsModel, CommentModel
from asgiref.sync import sync_to_async


@sync_to_async
def get_news():
    return list(NewsModel.objects.all().order_by("-created_at"))


@sync_to_async
def get_comments(news_id: int):
    return list(CommentModel.objects.filter(news_id=news_id).select_related("user").order_by("created_at"))
