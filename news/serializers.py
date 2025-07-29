from rest_framework import serializers
from .models import NewsModel, CommentModel


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CommentModel
        fields = ["id", "user", "message", "created_at"]


class NewsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NewsModel
        fields = ["id", "user", "title", "content", "created_at"]


class NewsDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = NewsModel
        fields = ["id", "user", "title", "content", "created_at", "comments"]
