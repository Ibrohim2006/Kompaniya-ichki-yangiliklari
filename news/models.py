from django.db import models
from authentication.models import TimeStampedModel, UserModel


class NewsModel(TimeStampedModel, models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class CommentModel(TimeStampedModel, models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="comments")
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, related_name="comments")
    message = models.TextField()

    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"Comment by {self.user.email} on {self.news.title}"
