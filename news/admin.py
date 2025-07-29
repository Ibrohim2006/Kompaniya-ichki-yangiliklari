from django.contrib import admin
from news.models import NewsModel, CommentModel

admin.site.register(NewsModel)
admin.site.register(CommentModel)
